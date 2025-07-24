import os
import logging
from typing import List, Dict, Any, Optional
from pathlib import Path
import frontmatter
import chromadb
from chromadb.config import Settings
from sentence_transformers import SentenceTransformer
from config import settings

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class PortfolioVectorDB:
    """Vector database for Mohammed Rishin's portfolio using ChromaDB."""
    
    def __init__(self, portfolio_path: str = None):
        self.portfolio_path = portfolio_path or settings.PORTFOLIO_DATA_PATH
        self.db_path = settings.VECTOR_DB_PATH
        self.embedding_model = SentenceTransformer(settings.EMBEDDING_MODEL)
        self.client = None
        self.collections = {}
        self._initialize_db()
    
    def _initialize_db(self) -> None:
        """Initialize ChromaDB client and collections."""
        try:
            # Create persistent ChromaDB client
            self.client = chromadb.PersistentClient(
                path=self.db_path,
                settings=Settings(
                    anonymized_telemetry=False,
                    allow_reset=True
                )
            )
            
            # Initialize collections for each category
            for category in settings.CONTENT_CATEGORIES:
                collection_name = f"portfolio_{category}"
                try:
                    self.collections[category] = self.client.get_collection(collection_name)
                    logger.info(f"Loaded existing collection: {collection_name}")
                except ValueError:
                    self.collections[category] = self.client.create_collection(
                        name=collection_name,
                        metadata={"category": category}
                    )
                    logger.info(f"Created new collection: {collection_name}")
            
            # Create unified collection for cross-category search
            try:
                self.collections['unified'] = self.client.get_collection("portfolio_unified")
                logger.info("Loaded existing unified collection")
            except ValueError:
                self.collections['unified'] = self.client.create_collection(
                    name="portfolio_unified",
                    metadata={"category": "unified"}
                )
                logger.info("Created new unified collection")
                
        except Exception as e:
            logger.error(f"Failed to initialize ChromaDB: {e}")
            raise
    
    def _chunk_text(self, text: str, chunk_size: int = None, overlap: int = None) -> List[str]:
        """Intelligently chunk text while preserving structure."""
        chunk_size = chunk_size or settings.CHUNK_SIZE
        overlap = overlap or settings.CHUNK_OVERLAP
        
        if len(text) <= chunk_size:
            return [text]
        
        chunks = []
        start = 0
        
        while start < len(text):
            end = start + chunk_size
            
            if end >= len(text):
                chunks.append(text[start:])
                break
            
            # Try to break at sentence or paragraph boundaries
            break_points = [
                text.rfind('\n\n', start, end),  # Paragraph break
                text.rfind('\n', start, end),    # Line break
                text.rfind('. ', start, end),    # Sentence end
                text.rfind(', ', start, end),    # Comma
                text.rfind(' ', start, end)      # Word boundary
            ]
            
            break_point = next((bp for bp in break_points if bp > start), end)
            chunks.append(text[start:break_point])
            start = break_point - overlap if break_point - overlap > start else break_point
        
        return [chunk.strip() for chunk in chunks if chunk.strip()]
    
    def _process_markdown_file(self, file_path: Path) -> Dict[str, Any]:
        """Process a markdown file and extract metadata and content."""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                post = frontmatter.load(f)
            
            # Extract metadata
            metadata = dict(post.metadata)
            content = post.content
            
            # Add file information
            metadata.update({
                'file_path': str(file_path),
                'filename': file_path.name,
                'category': file_path.parent.name,
                'file_size': file_path.stat().st_size,
                'last_modified': file_path.stat().st_mtime
            })
            
            return {
                'metadata': metadata,
                'content': content,
                'full_text': f"# {metadata.get('title', file_path.stem)}\n\n{content}"
            }
            
        except Exception as e:
            logger.error(f"Error processing file {file_path}: {e}")
            return None
    
    def _extract_technologies(self, content: str, metadata: Dict[str, Any]) -> List[str]:
        """Extract technology keywords from content and metadata."""
        technologies = set()
        
        # From metadata
        if 'technologies' in metadata:
            if isinstance(metadata['technologies'], list):
                technologies.update(tech.lower() for tech in metadata['technologies'])
            elif isinstance(metadata['technologies'], str):
                technologies.update(tech.strip().lower() for tech in metadata['technologies'].split(','))
        
        # Common technology patterns in content
        tech_patterns = [
            'node.js', 'nodejs', 'react', 'python', 'typescript', 'javascript',
            'fastapi', 'django', 'flask', 'mongodb', 'postgresql', 'mysql',
            'docker', 'kubernetes', 'aws', 'gcp', 'azure', 'tensorflow',
            'pytorch', 'opencv', 'scikit-learn', 'pandas', 'numpy',
            'express', 'vue', 'angular', 'next.js', 'nuxt', 'svelte'
        ]
        
        content_lower = content.lower()
        for tech in tech_patterns:
            if tech in content_lower:
                technologies.add(tech)
        
        return list(technologies)
    
    def add_document(self, file_path: Path) -> bool:
        """Add a single document to the vector database."""
        try:
            doc_data = self._process_markdown_file(file_path)
            if not doc_data:
                return False
            
            content = doc_data['content']
            metadata = doc_data['metadata']
            full_text = doc_data['full_text']
            category = metadata['category']
            
            # Extract technologies
            technologies = self._extract_technologies(content, metadata)
            metadata['technologies'] = technologies
            
            # Chunk the content
            chunks = self._chunk_text(full_text)
            
            for i, chunk in enumerate(chunks):
                # Create unique ID for each chunk
                chunk_id = f"{category}_{file_path.stem}_{i}"
                
                # Generate embedding
                embedding = self.embedding_model.encode([chunk]).tolist()[0]
                
                # Prepare chunk metadata
                chunk_metadata = metadata.copy()
                chunk_metadata.update({
                    'chunk_id': chunk_id,
                    'chunk_index': i,
                    'total_chunks': len(chunks),
                    'chunk_text': chunk[:200] + "..." if len(chunk) > 200 else chunk
                })
                
                # Convert list values to strings for ChromaDB compatibility
                for key, value in chunk_metadata.items():
                    if isinstance(value, list):
                        chunk_metadata[key] = ', '.join(str(v) for v in value)
                    elif not isinstance(value, (str, int, float, bool)):
                        chunk_metadata[key] = str(value)
                
                # Add to category-specific collection
                if category in self.collections:
                    self.collections[category].add(
                        embeddings=[embedding],
                        documents=[chunk],
                        metadatas=[chunk_metadata],
                        ids=[chunk_id]
                    )
                
                # Add to unified collection
                self.collections['unified'].add(
                    embeddings=[embedding],
                    documents=[chunk],
                    metadatas=[chunk_metadata],
                    ids=[chunk_id]
                )
            
            logger.info(f"Added {len(chunks)} chunks from {file_path.name} to {category} collection")
            return True
            
        except Exception as e:
            logger.error(f"Error adding document {file_path}: {e}")
            return False
    
    def process_all_content(self) -> Dict[str, int]:
        """Process all portfolio content and populate the vector database."""
        stats = {'total_files': 0, 'successful': 0, 'failed': 0, 'total_chunks': 0}
        
        portfolio_dir = Path(self.portfolio_path)
        
        for category in settings.CONTENT_CATEGORIES:
            category_dir = portfolio_dir / category
            
            if not category_dir.exists():
                logger.warning(f"Category directory not found: {category_dir}")
                continue
            
            for file_path in category_dir.glob("*.md"):
                stats['total_files'] += 1
                
                if self.add_document(file_path):
                    stats['successful'] += 1
                else:
                    stats['failed'] += 1
        
        # Calculate total chunks across all collections
        for category in settings.CONTENT_CATEGORIES:
            if category in self.collections:
                count = self.collections[category].count()
                stats['total_chunks'] += count
                logger.info(f"{category} collection: {count} chunks")
        
        unified_count = self.collections['unified'].count()
        logger.info(f"Unified collection: {unified_count} chunks")
        
        return stats
    
    def search_similar(self, query: str, category: Optional[str] = None, 
                      n_results: int = 5, technologies: Optional[List[str]] = None) -> List[Dict[str, Any]]:
        """Search for similar content in the vector database."""
        try:
            # Generate query embedding
            query_embedding = self.embedding_model.encode([query]).tolist()[0]
            
            # Choose collection
            collection = self.collections.get(category, self.collections['unified'])
            
            # Prepare where filter for technologies
            where_filter = None
            if technologies:
                # ChromaDB filter for technologies (simplified approach)
                where_filter = {"category": category} if category else None
            
            # Perform similarity search
            results = collection.query(
                query_embeddings=[query_embedding],
                n_results=n_results,
                where=where_filter
            )
            
            # Format results
            formatted_results = []
            for i in range(len(results['ids'][0])):
                formatted_results.append({
                    'id': results['ids'][0][i],
                    'document': results['documents'][0][i],
                    'metadata': results['metadatas'][0][i],
                    'distance': results['distances'][0][i] if 'distances' in results else None,
                    'relevance_score': 1 - results['distances'][0][i] if 'distances' in results else 1.0
                })
            
            return formatted_results
            
        except Exception as e:
            logger.error(f"Error searching similar content: {e}")
            return []
    
    def get_statistics(self) -> Dict[str, Any]:
        """Get database statistics."""
        stats = {
            'collections': {},
            'total_documents': 0,
            'categories': list(settings.CONTENT_CATEGORIES)
        }
        
        for category in settings.CONTENT_CATEGORIES + ['unified']:
            if category in self.collections:
                count = self.collections[category].count()
                stats['collections'][category] = count
                if category != 'unified':
                    stats['total_documents'] += count
        
        return stats
    
    def refresh_database(self) -> Dict[str, Any]:
        """Clear and rebuild the entire vector database."""
        logger.info("Refreshing vector database...")
        
        # Reset all collections
        for category in settings.CONTENT_CATEGORIES + ['unified']:
            if category in self.collections:
                try:
                    self.client.delete_collection(f"portfolio_{category}" if category != 'unified' else "portfolio_unified")
                except ValueError:
                    pass  # Collection doesn't exist
        
        # Reinitialize
        self._initialize_db()
        
        # Reprocess all content
        return self.process_all_content()

if __name__ == "__main__":
    # Example usage
    db = PortfolioVectorDB()
    
    # Refresh database
    stats = db.refresh_database()
    print(f"Database populated with {stats['successful']} files, {stats['total_chunks']} chunks")
    
    # Test search
    results = db.search_similar("nodejs projects", n_results=3)
    print(f"\nFound {len(results)} similar documents for 'nodejs projects'")
    for result in results:
        print(f"- {result['metadata']['filename']} (score: {result['relevance_score']:.3f})")