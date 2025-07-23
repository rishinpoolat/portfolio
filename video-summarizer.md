# Video Summarizer

**A comprehensive YouTube video summarization system with multi-LLM support, advanced web scraping, and Telegram bot integration**

## Overview

Video Summarizer is a sophisticated Node.js/TypeScript application that automatically generates intelligent summaries of YouTube videos using a combination of advanced web scraping, transcript extraction, and multiple AI providers. The system features a robust REST API with comprehensive N8N workflow integration and Telegram bot functionality for seamless automation.

## Core Architecture & Technical Highlights

### Advanced Web Scraping with Puppeteer
The system employs **Puppeteer** for sophisticated browser automation and dynamic content extraction:

- **Headless Browser Management**: Automated Chrome instances for JavaScript-heavy YouTube pages
- **Dynamic Content Loading**: Handles YouTube's dynamic loading of video metadata and transcripts
- **Anti-Detection Mechanisms**: Implements stealth browsing techniques to avoid rate limiting
- **Memory Management**: Automatic cleanup of browser instances to prevent memory leaks
- **Cookie & Session Handling**: Maintains session state for consistent data extraction

### Intelligent Transcript Extraction
The transcript extraction system is a core technical achievement:

- **Multiple Transcript Sources**: Handles both auto-generated and manual captions
- **Language Detection**: Automatically identifies transcript language and encoding
- **Chunked Processing**: Splits long transcripts into optimal chunks for AI processing
- **Format Normalization**: Converts various YouTube transcript formats to standardized text
- **Error Recovery**: Fallback mechanisms when transcripts are unavailable or corrupted
- **Timing Information**: Preserves timestamp data for potential future features

### Multi-LLM Provider System
Sophisticated AI provider management with automatic failover:

- **Priority-Based Routing**: Groq → OpenAI → Anthropic → Google Gemini
- **Dynamic Load Balancing**: Automatically switches providers based on availability
- **Rate Limit Handling**: Intelligent backoff and retry mechanisms
- **Cost Optimization**: Prioritizes free/cheaper providers while maintaining quality
- **Provider Health Monitoring**: Real-time status checking and failover logic

## Key Features

### Core Functionality
- **🤖 Multi-LLM Support**: Automatic failover across Groq, OpenAI, Anthropic, and Google Gemini
- **🕷️ Advanced Web Scraping**: Puppeteer-powered dynamic content extraction from YouTube
- **📝 Intelligent Transcript Processing**: Handles auto-generated and manual captions with smart chunking
- **🔄 Flexible Input Methods**: Process videos by channel name, channel URL, or direct video URL
- **⚡ High Performance**: Optimized chunked processing for long videos with intelligent rate limiting
- **🔍 Auto-Discovery**: Automatically finds and processes latest videos from YouTube channels
- **🛡️ Comprehensive Error Handling**: Multi-layered validation and error recovery mechanisms
- **📊 Health Monitoring**: Built-in health check and system monitoring endpoints

### Advanced Automation Features
- **🔗 N8N Workflow Integration**: Complete workflow automation system
- **📱 Telegram Bot Interface**: Full-featured bot with text and audio responses
- **🎵 Text-to-Speech Integration**: Support for OpenAI TTS and ElevenLabs
- **📈 Usage Analytics**: Built-in tracking and monitoring capabilities
- **🔧 Configurable Processing**: Customizable summarization parameters and formats

## REST API Architecture

### Endpoint Structure
```
GET  /              # API information and available endpoints
GET  /health        # Health check with detailed system metrics
POST /summarize     # Unified endpoint for channel or video URL processing
POST /summarize/video # Dedicated video URL processing endpoint
```

### Request/Response Patterns
```typescript
// Unified Request Format
interface SummarizeRequest {
  channel?: string;     // Channel name or URL
  videoUrl?: string;    // Direct video URL
}

// Standardized Response Format
interface APIResponse<T> {
  success: boolean;
  data?: T;
  error?: string;
  timestamp: string;
}

// Summary Response Data
interface SummaryData {
  title: string;
  summary: string;
  videoUrl: string;
  channelName: string;
  provider: string;
  processingTime?: number;
  transcriptLength?: number;
}
```

## N8N Workflow Integration

### Complete Telegram Bot System
The project includes a comprehensive **N8N workflow** that transforms the API into a fully functional Telegram bot:

#### Bot Features
- **🎬 Video Summarization**: Get summaries of latest videos from YouTube channels
- **📝 Formatted Text Responses**: Clean, structured summary presentation
- **🔊 Audio Summaries**: Text-to-speech conversion with multiple voice options
- **⚡ Multiple TTS Providers**: Choose between OpenAI TTS or ElevenLabs
- **🛡️ Error Handling**: Comprehensive error messages and user feedback
- **📊 Usage Analytics**: Built-in tracking and monitoring capabilities

#### Workflow Architecture
The N8N workflow consists of 12+ interconnected nodes:

1. **Telegram Trigger**: Webhook-based message reception
2. **Command Processing**: Handles `/start`, `/help`, and other commands
3. **Input Validation**: Validates and normalizes channel requests
4. **User Feedback**: Real-time processing status updates
5. **API Integration**: Calls the Video Summarizer API
6. **Response Processing**: Formats API responses for display
7. **Text Summary Delivery**: Sends formatted text summaries
8. **Audio Generation**: TTS conversion with provider selection
9. **Audio Delivery**: Sends MP3 files to users
10. **Error Handling**: Comprehensive error messaging
11. **Analytics Logging**: Usage tracking and monitoring
12. **Rate Limiting**: Built-in abuse prevention

#### TTS Integration Options
**OpenAI TTS Integration:**
- Multiple voice options (alloy, echo, fable, onyx, nova, shimmer)
- Adjustable speed and quality settings
- Cost-effective pricing (~$0.015 per 1K characters)
- High-quality HD models available

**ElevenLabs Integration:**
- Premium voice quality with natural speech patterns
- Voice cloning and custom voice options
- Advanced voice settings (stability, similarity, style)
- Speaker boost for enhanced clarity

### Workflow Configuration & Customization
```javascript
// Example TTS Configuration
{
  "openai": {
    "model": "tts-1-hd",
    "voice": "nova",
    "speed": 1.0
  },
  "elevenlabs": {
    "voice_settings": {
      "stability": 0.5,
      "similarity_boost": 0.75,
      "style": 0.5,
      "use_speaker_boost": true
    }
  }
}
```

## Technical Architecture Deep Dive

### Project Structure
```
src/
├── api/
│   └── server.ts              # Hono-based API server
├── services/
│   ├── ai.service.ts          # Multi-LLM provider management
│   ├── summary.service.ts     # Core summarization logic
│   ├── youtube.service.ts     # YouTube data extraction
│   └── transcript.service.ts  # Advanced transcript processing
├── utils/
│   ├── logger.ts              # Winston-based logging system
│   └── puppeteer-manager.ts   # Browser automation management
├── config/
│   └── constants.ts           # System configuration
└── types/
    └── index.ts               # TypeScript definitions
```

### Technology Stack
- **Runtime Environment**: Bun (primary) / Node.js with TypeScript
- **Web Framework**: Hono for lightweight, high-performance API handling
- **Browser Automation**: Puppeteer for dynamic content scraping
- **AI Integration**: Multi-provider SDK integration (OpenAI, Anthropic, Google, Groq)
- **Validation**: Zod for runtime type checking and request validation
- **Logging**: Winston for structured logging and monitoring
- **Workflow Automation**: N8N for complex automation pipelines

### Advanced Puppeteer Implementation
```typescript
// Example of advanced browser management
class PuppeteerManager {
  private browserInstances: Map<string, Browser> = new Map();
  
  async createBrowser(options: BrowserOptions): Promise<Browser> {
    // Stealth configuration for YouTube compatibility
    const browser = await puppeteer.launch({
      headless: true,
      args: [
        '--no-sandbox',
        '--disable-setuid-sandbox',
        '--disable-dev-shm-usage',
        '--disable-gpu',
        '--no-first-run'
      ]
    });
    
    // Anti-detection measures
    const page = await browser.newPage();
    await page.setUserAgent('Mozilla/5.0...');
    await page.setViewport({ width: 1920, height: 1080 });
    
    return browser;
  }
  
  async extractTranscript(videoUrl: string): Promise<TranscriptData> {
    // Complex transcript extraction logic
    // Handles multiple YouTube transcript formats
    // Implements retry logic and error recovery
  }
}
```

### Transcript Processing Pipeline
1. **URL Analysis**: Validates and normalizes YouTube URLs
2. **Browser Launch**: Creates optimized Puppeteer instance
3. **Page Navigation**: Loads video page with error handling
4. **Transcript Discovery**: Locates available transcript formats
5. **Data Extraction**: Extracts and normalizes transcript text
6. **Chunking Strategy**: Intelligently splits long transcripts
7. **Language Processing**: Handles multiple languages and encodings
8. **Quality Validation**: Ensures transcript completeness and accuracy

## Usage Examples & Integration Patterns

### Direct API Usage
```bash
# Channel-based summarization
curl -X POST http://localhost:3000/summarize \
  -H "Content-Type: application/json" \
  -d '{"channel": "Fireship"}'

# Direct video URL processing
curl -X POST http://localhost:3000/summarize/video \
  -H "Content-Type: application/json" \
  -d '{"url": "https://youtube.com/watch?v=dQw4w9WgXcQ"}'
```

### Telegram Bot Usage
```
User: Fireship
Bot: 🔄 Processing your request for: Fireship
Bot: 🎬 **I tried 8 different programming languages**
     📺 Channel: Fireship
     ⏱️ Duration: 8:32
     📝 Summary: In this comprehensive comparison, the creator explores 8 different programming languages by building the same project in each...
     [Detailed summary continues...]
Bot: 🔊 [Audio file: summary.mp3]
```

### N8N Workflow Integration
The system provides complete workflow templates for:
- **Scheduled Processing**: Automatic summarization of new videos
- **Batch Processing**: Bulk channel analysis and reporting
- **Custom Integrations**: Webhook-based third-party service integration
- **Analytics Pipelines**: Usage tracking and performance monitoring

## Production Deployment & Scaling

### Performance Optimizations
- **Connection Pooling**: Efficient browser instance management
- **Caching Layer**: Intelligent caching of frequently requested summaries
- **Rate Limiting**: Built-in protection against abuse and API limits
- **Resource Management**: Automatic cleanup and memory optimization
- **Monitoring**: Comprehensive health checks and performance metrics

### Security Considerations
- **API Key Management**: Secure credential handling and rotation
- **Input Validation**: Comprehensive request sanitization
- **Rate Limiting**: Protection against abuse and DOS attacks
- **Error Handling**: Secure error messages without information leakage
- **Browser Security**: Sandboxed Puppeteer execution

### Monitoring & Analytics
- **Real-time Metrics**: Processing times, success rates, error patterns
- **Cost Tracking**: AI provider usage and cost optimization
- **User Analytics**: Usage patterns and popular content analysis
- **System Health**: Resource utilization and performance monitoring

## Use Cases & Applications

### Content Creation & Research
- **Competitive Analysis**: Monitor competitor content and trends
- **Research Automation**: Process educational and tutorial content
- **Content Curation**: Generate summaries for content aggregation
- **SEO Research**: Analyze trending topics and keywords

### Business Intelligence
- **Market Research**: Track industry discussions and developments
- **Training Material**: Create summaries of educational content
- **Documentation**: Generate documentation from tutorial videos
- **Knowledge Management**: Build searchable knowledge bases

### Personal Productivity
- **Learning Optimization**: Quick summaries of lengthy tutorials
- **News Consumption**: Efficient processing of news content
- **Skill Development**: Condensed learning from educational channels
- **Time Management**: Quick content evaluation before watching

This project demonstrates advanced expertise in web scraping, API design, multi-provider integration, workflow automation, and creating production-ready systems with comprehensive monitoring and error handling capabilities.