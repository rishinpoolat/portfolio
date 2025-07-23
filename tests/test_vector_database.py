import pytest
import tempfile
import shutil
from pathlib import Path
from vector_database import PortfolioVectorDB
from config import settings

class TestPortfolioVectorDB:
    """Test cases for PortfolioVectorDB functionality."""
    
    @pytest.fixture
    def temp_portfolio_dir(self):
        """Create a temporary portfolio directory with sample files."""
        temp_dir = tempfile.mkdtemp()
        portfolio_path = Path(temp_dir)
        
        # Create category directories
        for category in settings.CONTENT_CATEGORIES:
            category_dir = portfolio_path / category
            category_dir.mkdir(exist_ok=True)
            
            # Create a sample markdown file for each category
            if category == "projects":
                sample_content = """---
title: Sample Node.js Project
technologies: [Node.js, Express, MongoDB]
date: 2023-01-01
---

# Sample Node.js Project

This is a sample project built with Node.js and Express.js. It demonstrates 
REST API development and database integration with MongoDB.

## Features
- User authentication
- CRUD operations
- Real-time updates

## Technologies Used
- Node.js for backend
- Express.js for web framework
- MongoDB for database
"""
            elif category == "education":
                sample_content = """---
title: Computer Science Degree
institution: Sample University
degree: Bachelor of Science
graduation_date: 2022-05-15
---

# Bachelor of Science in Computer Science

Completed my undergraduate degree at Sample University with focus on 
software engineering and artificial intelligence.

## Coursework
- Data Structures and Algorithms
- Machine Learning
- Software Engineering
- Database Systems
"""
            else:
                sample_content = f"""---
title: Sample {category.title()}
category: {category}
---

# Sample {category.title()}

This is sample content for the {category} category.
"""
            
            sample_file = category_dir / f"sample_{category}.md"
            sample_file.write_text(sample_content)
        
        yield str(portfolio_path)
        
        # Cleanup
        shutil.rmtree(temp_dir)
    
    @pytest.fixture
    def vector_db(self, temp_portfolio_dir):
        """Create a PortfolioVectorDB instance with temporary data."""
        # Use temporary database path
        temp_db_dir = tempfile.mkdtemp()
        original_db_path = settings.VECTOR_DB_PATH
        settings.VECTOR_DB_PATH = temp_db_dir
        
        try:
            db = PortfolioVectorDB(portfolio_path=temp_portfolio_dir)
            yield db
        finally:
            # Restore original settings
            settings.VECTOR_DB_PATH = original_db_path
            shutil.rmtree(temp_db_dir)
    
    def test_initialization(self, vector_db):
        """Test that the vector database initializes properly."""
        assert vector_db.client is not None
        assert len(vector_db.collections) == len(settings.CONTENT_CATEGORIES) + 1  # +1 for unified
        
        # Check that all expected collections exist
        for category in settings.CONTENT_CATEGORIES:
            assert category in vector_db.collections
        assert 'unified' in vector_db.collections
    
    def test_process_all_content(self, vector_db):
        """Test processing all content from the portfolio."""
        stats = vector_db.process_all_content()
        
        assert stats['total_files'] == len(settings.CONTENT_CATEGORIES)
        assert stats['successful'] > 0
        assert stats['failed'] == 0
        assert stats['total_chunks'] > 0
    
    def test_search_functionality(self, vector_db):
        """Test searching for content in the vector database."""
        # First populate the database
        vector_db.process_all_content()
        
        # Test general search
        results = vector_db.search_similar("node.js project", n_results=3)
        assert len(results) <= 3
        assert all('relevance_score' in result for result in results)
        
        # Test category-specific search
        project_results = vector_db.search_similar("project", category="projects", n_results=2)
        assert len(project_results) <= 2
        
        # Verify results contain expected metadata
        if results:
            result = results[0]
            assert 'metadata' in result
            assert 'document' in result
            assert 'id' in result
    
    def test_get_statistics(self, vector_db):
        """Test getting database statistics."""
        # Populate database first
        vector_db.process_all_content()
        
        stats = vector_db.get_statistics()
        
        assert 'collections' in stats
        assert 'total_documents' in stats
        assert 'categories' in stats
        assert stats['categories'] == list(settings.CONTENT_CATEGORIES)
        assert stats['total_documents'] > 0
    
    def test_technology_extraction(self, vector_db):
        """Test technology extraction from content and metadata."""
        # Create a test file path
        test_file = Path(vector_db.portfolio_path) / "projects" / "sample_projects.md"
        
        # Test the document processing
        doc_data = vector_db._process_markdown_file(test_file)
        assert doc_data is not None
        
        # Check that technologies are extracted
        technologies = vector_db._extract_technologies(doc_data['content'], doc_data['metadata'])
        assert isinstance(technologies, list)
        # Should find "node.js" and "mongodb" from the sample content
        assert any('node' in tech.lower() for tech in technologies)
    
    def test_chunking_functionality(self, vector_db):
        """Test text chunking with different sizes."""
        sample_text = "This is a test. " * 100  # Create long text
        
        # Test with default settings
        chunks = vector_db._chunk_text(sample_text)
        assert len(chunks) > 1
        assert all(len(chunk) <= settings.CHUNK_SIZE + settings.CHUNK_OVERLAP for chunk in chunks)
        
        # Test with custom chunk size
        small_chunks = vector_db._chunk_text(sample_text, chunk_size=50, overlap=10)
        assert len(small_chunks) > len(chunks)
    
    def test_refresh_database(self, vector_db):
        """Test database refresh functionality."""
        # First populate
        initial_stats = vector_db.process_all_content()
        
        # Then refresh
        refresh_stats = vector_db.refresh_database()
        
        # Stats should be similar after refresh
        assert refresh_stats['total_files'] == initial_stats['total_files']
        assert refresh_stats['successful'] == initial_stats['successful']

if __name__ == "__main__":
    pytest.main([__file__, "-v"])