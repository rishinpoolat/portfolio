import {
  Project,
  Experience,
  Education,
  Certification,
  Hackathon,
} from "../types/portfolio";

// Legacy interfaces for backward compatibility
export interface TimelineItem {
  id: string;
  date: string;
  title: string;
  organization: string;
  location: string;
  type: "education" | "experience";
}

export const projects: Project[] = [
  {
    id: "commit-suggester",
    title: "Commit Suggester",
    shortDescription:
      "Commit Suggester is an intelligent CLI tool that revolutionizes your git workflow by automatically generating conventional commit messages using AI. Instead of struggling to write meaningful commit messages, this tool analyzes your staged changes and provides AI-powered suggestions that follow conventional commit standards",
    fullDescription:
      "Intelligent CLI tool that revolutionizes git workflow by automatically generating conventional commit messages using AI. Supports multiple AI providers with automatic failover.",
    githubUrl: "https://github.com/rishinpoolat/commit-suggester",
    technologies: ["TypeScript", "Bun", "Node.js", "AI/ML", "CLI"],
    techStack: [
      { category: "Runtime", technologies: ["Bun", "TypeScript"] },
      {
        category: "AI Providers",
        technologies: ["Groq", "OpenAI", "Anthropic", "Google Gemini"],
      },
      {
        category: "Libraries",
        technologies: ["inquirer.js", "chalk", "axios"],
      },
    ],
    features: [
      {
        title: "Multi-Provider AI Support",
        description:
          "Support for multiple AI providers with automatic failover",
        details: [
          "Groq (recommended)",
          "OpenAI",
          "Anthropic Claude",
          "Google Gemini",
        ],
      },
      {
        title: "Intelligent Workflow Modes",
        description: "Auto and interactive modes for different use cases",
        details: [
          "Auto Mode (default)",
          "Interactive Mode (-i flag)",
          "Custom message options",
        ],
      },
    ],
    achievements: [
      { metric: "99% accuracy", description: "in commit message generation" },
      { metric: "4 AI providers", description: "with automatic failover" },
      { metric: "NPM package", description: "published globally" },
    ],
    challenges: [
      "Multi-provider integration",
      "Git diff parsing",
      "Error handling",
    ],
    solutions: [
      "Unified AI interface",
      "Robust parsing logic",
      "Comprehensive error recovery",
    ],
    learnings: [
      "AI integration patterns",
      "CLI tool development",
      "Package distribution",
    ],
    category: "cli-tool",
    complexity: "advanced",
    status: "completed",
  },
  {
    id: "smart-renamer",
    title: "Smart Renamer",
    description:
      "Built intelligent CLI tool for maintaining file naming consistency across projects with smart convention detection, interactive renaming, and real-time file monitoring. Supports multiple naming patterns (camelCase, kebab-case, snake_case) with automatic exclusions for config files and smart project analysis.",
    techStack: ["TypeScript", "Bun", "Commander.js", "Chokidar", "Inquirer.js"],
    githubUrl: "https://github.com/rishinpoolat/renamer",
    fullDescription:
      "Smart Renamer is a powerful CLI tool designed to maintain consistent file naming conventions across entire projects. It intelligently detects existing naming patterns and provides seamless renaming capabilities with real-time monitoring.",
    features: [
      "Intelligent naming convention detection",
      "Support for camelCase, kebab-case, snake_case, and PascalCase",
      "Real-time file monitoring with Chokidar",
      "Interactive renaming with preview and confirmation",
      "Automatic exclusion of configuration files",
      "Batch renaming capabilities",
      "Project structure analysis",
    ],
    challenges: [
      "Accurately detecting existing naming conventions in mixed codebases",
      "Handling edge cases with special file types",
      "Implementing safe renaming without breaking imports",
      "Creating efficient file watching mechanisms",
    ],
    achievements: [
      "Maintains consistency across large codebases",
      "Reduces manual renaming effort by 90%",
      "Zero breaking changes to existing imports",
      "Fast performance with Bun runtime",
    ],
  },
  {
    id: "video-summarizer",
    title: "Video Summarizer",
    shortDescription:
      "Sophisticated YouTube video summarization system with multi-LLM support, advanced web scraping, and Telegram bot integration for intelligent content processing.",
    description:
      "Developed video summarization REST API with multi-LLM orchestration and n8n workflow integration, featuring intelligent failover and advanced chunking algorithms, attaining 95% transcript accuracy and decreased content consumption time by 85%.",
    technologies: ["TypeScript", "Bun", "Hono", "Puppeteer", "N8N", "AI/ML"],
    githubUrl: "https://github.com/rishinpoolat/video-summarizer",
    fullDescription:
      "Video Summarizer is a comprehensive YouTube video summarization system that automatically generates intelligent summaries using a combination of advanced web scraping, transcript extraction, and multiple AI providers. Features robust REST API with N8N workflow integration and Telegram bot functionality for seamless automation.",
    features: [
      {
        title: "Multi-LLM Provider System",
        description:
          "Sophisticated AI provider management with automatic failover",
        details: [
          "Priority-based routing: Groq → OpenAI → Anthropic → Google Gemini",
          "Dynamic load balancing based on availability",
          "Rate limit handling with intelligent backoff",
          "Cost optimization prioritizing free/cheaper providers",
          "Real-time provider health monitoring",
        ],
      },
      {
        title: "Advanced Web Scraping",
        description: "Puppeteer-powered sophisticated browser automation",
        details: [
          "Headless browser management for JavaScript-heavy pages",
          "Anti-detection mechanisms to avoid rate limiting",
          "Memory management with automatic cleanup",
          "Cookie & session handling for consistent extraction",
          "Dynamic content loading for YouTube metadata",
        ],
      },
      {
        title: "Intelligent Transcript Processing",
        description: "Advanced transcript extraction and processing system",
        details: [
          "Multiple transcript sources (auto-generated and manual)",
          "Language detection and encoding normalization",
          "Chunked processing for optimal AI processing",
          "Error recovery with fallback mechanisms",
          "Timing information preservation",
        ],
      },
      {
        title: "N8N Workflow Integration",
        description: "Complete Telegram bot system with automation",
        details: [
          "Comprehensive 12+ node workflow architecture",
          "Text-to-speech integration (OpenAI TTS & ElevenLabs)",
          "Real-time processing status updates",
          "Analytics logging and usage tracking",
          "Rate limiting and abuse prevention",
        ],
      },
    ],
    techStack: [
      { category: "Runtime", technologies: ["Bun", "Node.js", "TypeScript"] },
      { category: "Framework", technologies: ["Hono", "RESTful API"] },
      {
        category: "AI Providers",
        technologies: ["Groq", "OpenAI", "Anthropic", "Google Gemini"],
      },
      {
        category: "Automation",
        technologies: ["Puppeteer", "N8N", "Telegram Bot API"],
      },
      { category: "Libraries", technologies: ["Zod", "Winston", "Chokidar"] },
    ],
    challenges: [
      "Handling large video transcripts with token limitations",
      "Implementing reliable failover between different AI models",
      "Optimizing chunking algorithms for context preservation",
      "Managing concurrent video processing requests",
      "Creating stealth browsing techniques for YouTube scraping",
    ],
    achievements: [
      {
        metric: "95% accuracy",
        description: "transcript extraction and processing",
      },
      { metric: "85% reduction", description: "in content consumption time" },
      {
        metric: "4 AI providers",
        description: "with intelligent failover system",
      },
      {
        metric: "12+ nodes",
        description: "comprehensive N8N workflow integration",
      },
    ],
    solutions: [
      "Multi-provider AI orchestration with priority routing",
      "Advanced Puppeteer browser automation with anti-detection",
      "Intelligent chunking algorithms for context preservation",
      "Comprehensive N8N workflow for Telegram bot automation",
    ],
    learnings: [
      "Advanced web scraping and browser automation",
      "Multi-LLM integration and failover strategies",
      "Workflow automation with N8N",
      "API design for video processing systems",
    ],
    category: "other",
    complexity: "advanced",
    status: "completed",
  },
  {
    id: "automated-essay-scoring",
    title: "Automated Essay Scoring System",
    description:
      "Engineered hybrid automated essay scoring system combining DeBERTa ensemble with LightGBM feature models and calibration techniques, achieving 0.8358 QWK on 24,728 essays with comprehensive feedback generation and responsive web dashboard.",
    techStack: [
      "Python",
      "NLP",
      "DeBERTa",
      "Machine Learning",
      "FastAPI",
      "LightGBM",
    ],
    githubUrl: "https://github.com/rishinpoolat/automated-essay-scoring",
    fullDescription:
      "Advanced automated essay scoring system that combines state-of-the-art NLP models with traditional ML approaches to provide accurate essay assessments and detailed feedback.",
    features: [
      "Hybrid model architecture with DeBERTa and LightGBM",
      "Comprehensive essay analysis and scoring",
      "Detailed feedback generation",
      "Web dashboard for essay submission and review",
      "Calibration techniques for score accuracy",
      "Support for multiple essay types and rubrics",
    ],
    challenges: [
      "Balancing deep learning and traditional ML approaches",
      "Handling diverse essay styles and topics",
      "Ensuring fair and unbiased scoring across demographics",
      "Optimizing model performance for real-time scoring",
    ],
    achievements: [
      "0.8358 Quadratic Weighted Kappa (QWK) score",
      "Processed 24,728 essays in evaluation dataset",
      "Comprehensive feedback system",
      "Responsive web interface for educators",
    ],
  },
  {
    id: "ai-project-recommendation",
    title: "AI Project Recommendation System",
    description:
      "Built intelligent developer project recommendation platform using Next.js and Google Gemini AI, featuring hybrid search with PostgreSQL full-text search and AI-generated suggestions. Delivers personalized project ideas with detailed implementation steps, tech stacks, and learning outcomes based on user prompts.",
    techStack: [
      "Next.js",
      "TypeScript",
      "Google Gemini AI",
      "Supabase",
      "PostgreSQL",
      "Tailwind CSS",
      "Radix UI",
    ],
    githubUrl: "https://github.com/rishinpoolat/idea-solution-frontend",
    fullDescription:
      "An intelligent platform that helps developers discover and plan their next projects using AI-powered recommendations and comprehensive project analysis.",
    features: [
      "AI-powered project recommendations using Google Gemini",
      "Hybrid search combining PostgreSQL and AI",
      "Detailed implementation roadmaps",
      "Technology stack suggestions",
      "Learning outcome predictions",
      "Personalized recommendations based on skill level",
      "Modern UI with Tailwind CSS and Radix UI",
    ],
    challenges: [
      "Integrating AI recommendations with traditional search",
      "Creating comprehensive project analysis algorithms",
      "Designing intuitive user experience for complex data",
      "Balancing AI creativity with practical feasibility",
    ],
    achievements: [
      "Intelligent project matching algorithm",
      "Comprehensive implementation guidance",
      "Seamless full-stack integration",
      "User-friendly modern interface",
    ],
  },
  {
    id: "penply",
    title: "Penply",
    description:
      "Built unified collaborative study platform consolidating real-time chat, note sharing, file management, event scheduling, and calendar functionality into single interface, eliminating context switching by 75% with scalable architecture and cloud deployment.",
    techStack: [
      "JavaScript",
      "React",
      "TailwindCSS",
      "Node.js",
      "Express.js",
      "AWS",
      "EC2",
      "DynamoDB",
      "RDS",
      "S3",
    ],
    liveUrl: "http://www.penply.com",
    fullDescription:
      "Penply is a comprehensive collaborative study platform that brings together all essential student tools in one unified interface, reducing the need for context switching between multiple applications.",
    features: [
      "Real-time chat and messaging",
      "Collaborative note sharing and editing",
      "File management and storage",
      "Event scheduling and calendar integration",
      "User authentication and permissions",
      "Mobile-responsive design",
      "Cloud-based architecture",
    ],
    challenges: [
      "Implementing real-time features at scale",
      "Designing unified UX for multiple complex features",
      "Managing cloud infrastructure and costs",
      "Ensuring data security and privacy",
    ],
    achievements: [
      "75% reduction in context switching",
      "Scalable cloud deployment on AWS",
      "Integrated multiple complex features seamlessly",
      "Positive user feedback on unified experience",
    ],
  },
  {
    id: "helmet-detector",
    title: "Real-time Helmet Detector",
    description:
      "Developed a CNN model for detecting whether riders wearing helmets or not. The model was then integrated into a Raspberry Pi, camera, and speaker. The integration enabled real-time monitoring of helmet usage, with the camera capturing visual data, the ML model analyzing it, and the speaker providing immediate feedback based on the detection results.",
    techStack: [
      "Python",
      "TensorFlow",
      "Keras",
      "OpenCV",
      "Numpy",
      "Pandas",
      "MobileNetV2",
      "Raspberry Pi",
    ],
    githubUrl: "https://github.com/rishinpoolat/realtime-helmet-detector",
    fullDescription:
      "A computer vision system designed for traffic safety monitoring, using deep learning to detect helmet usage in real-time with immediate audio feedback.",
    features: [
      "Real-time helmet detection using CNN",
      "MobileNetV2 architecture for edge deployment",
      "Raspberry Pi integration for portable solution",
      "Camera integration for live video processing",
      "Audio feedback system for immediate alerts",
      "Optimized for edge computing performance",
    ],
    challenges: [
      "Optimizing deep learning models for Raspberry Pi",
      "Achieving real-time performance with limited compute",
      "Handling various lighting and angle conditions",
      "Integrating hardware components seamlessly",
    ],
    achievements: [
      "Successful edge deployment on Raspberry Pi",
      "Real-time detection with immediate feedback",
      "Practical application for traffic safety",
      "Efficient model optimization for edge devices",
    ],
  },
  {
    id: "from-home",
    title: "From Home",
    description:
      "The Full-Stack E-commerce web application is specifically designed to cater to the needs of home bakers, providing them with a platform where they can easily showcase and sell their delicious homemade products online, thereby bridging the gap between baking enthusiasts and potential customers.",
    techStack: ["React.js", "Node.js", "Express", "MongoDB"],
    githubUrl: "https://github.com/rishinpoolat/from-home",
    fullDescription:
      "A specialized e-commerce platform designed to empower home bakers by providing them with professional tools to showcase and sell their homemade products online.",
    features: [
      "Product catalog with image galleries",
      "Shopping cart and checkout system",
      "User authentication and profiles",
      "Order management system",
      "Payment integration",
      "Responsive design for all devices",
      "Admin panel for inventory management",
    ],
    challenges: [
      "Creating intuitive product showcase for food items",
      "Implementing secure payment processing",
      "Designing mobile-first responsive interface",
      "Managing complex state across the application",
    ],
    achievements: [
      "Complete e-commerce solution for niche market",
      "Seamless user experience from browsing to purchase",
      "Scalable architecture supporting growth",
      "Successfully bridges gap between bakers and customers",
    ],
  },
  {
    id: "wise-wallet",
    title: "Wise Wallet",
    description:
      "Receipt analysis application that extracts text from user-uploaded receipts using OCR technology, leveraging a fine-tuned AI model to provide personalized suggestions and feedback.",
    techStack: [
      "React.js",
      "Tailwind",
      "Cloud Firestore",
      "Firebase",
      "OCR",
      "AI/ML",
    ],
    liveUrl: "https://wisewallet-app.vercel.app/",
    fullDescription:
      "Wise Wallet is an intelligent receipt analysis application that helps users track their spending patterns and provides personalized financial insights using OCR and AI technologies.",
    features: [
      "OCR-powered receipt text extraction",
      "AI-driven spending analysis",
      "Personalized financial recommendations",
      "Cloud-based data storage with Firestore",
      "Real-time expense tracking",
      "Category-based expense organization",
      "Visual spending analytics",
    ],
    challenges: [
      "Implementing accurate OCR for various receipt formats",
      "Training AI models for financial analysis",
      "Ensuring data privacy and security",
      "Creating intuitive user interface for complex data",
    ],
    achievements: [
      "Finalist in IBM CIC Hackathon",
      "Accurate receipt text extraction across formats",
      "Meaningful financial insights generation",
      "Cloud-deployed scalable solution",
    ],
  },
  {
    id: "social-app",
    title: "SocialApp",
    shortDescription:
      "Comprehensive full-stack social media platform with advanced authentication, real-time interactions, and secure social networking features.",
    description:
      "The social media application provides users with the ability to follow their favorite accounts, share their thoughts through creating posts, express appreciation by liking content, and engage in discussions by commenting on posts shared within the platform.",
    technologies: [
      "Node.js",
      "Express.js",
      "PostgreSQL",
      "EJS",
      "JWT",
      "bcrypt",
      "Speakeasy",
    ],
    githubUrl: "https://github.com/rishinpoolat/socialapp",
    fullDescription:
      "SocialApp is a comprehensive full-stack social media platform designed to deliver an engaging and secure social networking experience. Built with modern web technologies, it provides users with essential social media features including advanced authentication with OTP verification, real-time posting capabilities, social interactions, and a robust follow system.",
    features: [
      {
        title: "Advanced Authentication System",
        description: "Multi-factor authentication with comprehensive security",
        details: [
          "OTP verification using Speakeasy for enhanced security",
          "Email verification with secure token generation",
          "Bcrypt password hashing with salt rounds",
          "JWT-based session management with secure cookies",
          "Password recovery and reset functionality",
        ],
      },
      {
        title: "Social Networking Core",
        description: "Complete social media functionality",
        details: [
          "Comprehensive user profile management",
          "Real-time post creation and sharing",
          "Like and comment system for engagement",
          "Follow/unfollow functionality",
          "Activity feed with posts from followed users",
        ],
      },
      {
        title: "Content Management",
        description: "Advanced content handling and moderation",
        details: [
          "Media upload support with Multer middleware",
          "Full CRUD operations for user-generated content",
          "Built-in content validation and security",
          "Responsive design for cross-device compatibility",
        ],
      },
      {
        title: "Communication Features",
        description: "Real-time interaction and engagement tools",
        details: [
          "Real-time notification system",
          "Hierarchical comment threads",
          "Advanced user search functionality",
          "Activity tracking and engagement metrics",
        ],
      },
    ],
    techStack: [
      {
        category: "Backend",
        technologies: ["Node.js", "Express.js", "PostgreSQL", "Sequelize ORM"],
      },
      {
        category: "Authentication",
        technologies: ["JWT", "bcrypt", "Speakeasy", "Nodemailer"],
      },
      {
        category: "Frontend",
        technologies: ["EJS", "Custom CSS", "JavaScript"],
      },
      {
        category: "DevOps",
        technologies: ["PM2", "ESLint", "Prettier", "dotenv"],
      },
    ],
    challenges: [
      "Implementing multi-factor authentication with OTP",
      "Managing complex database relationships efficiently",
      "Creating responsive UI with server-side rendering",
      "Handling concurrent user interactions and real-time features",
      "Ensuring data security and privacy compliance",
    ],
    achievements: [
      {
        metric: "Complete",
        description: "social media platform with all core features",
      },
      {
        metric: "Multi-factor",
        description: "authentication with OTP verification",
      },
      {
        metric: "Real-time",
        description: "notifications and user interactions",
      },
      { metric: "Scalable", description: "PostgreSQL database architecture" },
    ],
    solutions: [
      "Multi-layer security with JWT and OTP authentication",
      "Comprehensive database design with Sequelize ORM",
      "Server-side rendering with EJS for optimal performance",
      "PM2 process management for production deployment",
    ],
    learnings: [
      "Advanced authentication and security implementation",
      "Full-stack social media architecture",
      "Database relationship modeling",
      "Production deployment with PM2",
    ],
    category: "social",
    complexity: "advanced",
    status: "completed",
  },
];

export const timelineData: TimelineItem[] = [
  {
    id: "offseason-2025",
    date: "March 2025 - Present",
    title: "Software Engineer",
    organization: "OFFSeason",
    location: "Leicester, United Kingdom",
    type: "experience",
  },
  {
    id: "leicester-msc",
    date: "January 2024 - May 2025",
    title: "MSc Advanced Computer Science",
    organization: "University of Leicester",
    location: "Leicester, United Kingdom",
    type: "education",
  },
  {
    id: "qburst-2023",
    date: "July 2023 - December 2023",
    title: "Software Engineer",
    organization: "Qburst",
    location: "Kerala, India",
    type: "experience",
  },
  {
    id: "ktu-btech",
    date: "June 2019 - July 2023",
    title: "B.Tech Computer Science and Engineering",
    organization: "APJ Abdul Kalam Technological University",
    location: "Kerala, India",
    type: "education",
  },
];

export const experienceData: Experience[] = [
  {
    id: "offseason-2025",
    title: "Software Engineer",
    company: "OFFSeason",
    duration: "March 2025 - Present",
    location: "Leicester, United Kingdom",
    responsibilities: [
      "Architected e-commerce platform using Next.js, Stripe payments, Supabase, serving 2,000+ daily users with real-time inventory synchronization, automated email workflows via Trigger.dev, maintaining 99.5% uptime across revenue streams.",
      "Developed Tracy POS system with real-time inventory tracking across 2 locations, multi-payment processing, VAT management, barcode scanning, sales analytics, supporting 2,000+ daily transactions minimizing inventory discrepancies by 75%.",
      "Engineered AI agent ecosystem using LLMs, Model Context Protocol (MCP), n8n workflow orchestration, processing 500+ daily operations including order confirmations, payment failures, business notifications with 95% automation success rate.",
      "Implemented system architecture with TypeScript, PostgreSQL, Docker containerization, CI/CD pipelines, achieving zero-downtime deployments with integrated analytics dashboards for real-time business intelligence across retail operations.",
    ],
  },
  {
    id: "qburst-2023",
    title: "Software Engineer",
    company: "Qburst",
    duration: "July 2023 - December 2023",
    location: "Kerala, India",
    responsibilities: [
      "Led development of a high-impact CMS project with microservices architecture and comprehensive testing, built REST APIs using Node.js and React component libraries, maintaining 98% API uptime through CI/CD pipelines and Docker containerization.",
      "Established scalable file upload system with AWS S3, EC2, and CloudFront CDN distribution, implementing React hooks for state management, reducing storage costs by 30% and improving reliability through scheduled backup.",
      "Excelled in agile scrum collaboration methodologies and implemented comprehensive code quality monitoring tools with Jest unit testing framework attaining 85% test coverage rates. Resulted in a 40% boost in team efficiency and 95% task completion rate.",
      "Enhanced real-time communication using Socket.io and React with Redis caching and connection pooling, minimizing latency by 70% and implemented optimizations within PostgreSQL database, resulting in a 30% reduction in resource consumption.",
    ],
  },
];

export const educationData: Education[] = [
  {
    id: "leicester-msc",
    institution: "University of Leicester",
    degree: "MSc Advanced Computer Science",
    duration: "January 2024 - May 2025",
    location: "Leicester, United Kingdom",
    grade: "Distinction",
    description:
      "Master of Science in Advanced Computer Science with Distinction",
    details: {
      overview:
        "Advanced study of modern computer science paradigms including big data analytics, generative development, mobile and web applications, and distributed computing systems.",
      coreModules: [
        {
          name: "Big Data and Predictive Analytics (CO7093)",
          credits: 15,
          grade: "A (72.80%)",
          description:
            "Study of methods and tools for predictive analysis using scikit-learn and Apache Spark for statistical modeling, credit approval, marketing, and demand forecasting.",
        },
        {
          name: "Generative Development (CO7207)",
          credits: 15,
          grade: "A (78.95%)",
          description:
            "Advanced software engineering paradigms including UML modeling, generative methods, aspect-oriented programming, and Model-Driven Architecture (MDA).",
        },
        {
          name: "Mobile and Web Applications (CO7102)",
          credits: 15,
          grade: "A (75.76%)",
          description:
            "Comprehensive exploration of web technologies, mobile development, XML techniques, security, Java servlets, JavaScript, and web services.",
        },
        {
          name: "Internet and Cloud Computing (CO7219)",
          credits: 15,
          grade: "A (75.36%)",
          description:
            "Networking fundamentals, cloud computing principles, MapReduce programming, Hadoop implementation, and cloud security considerations.",
        },
        {
          name: "Software Measurement and Quality Assurance (CO7095)",
          credits: 15,
          grade: "A (70.89%)",
          description:
            "Industrial software quality assurance, software metrics, testing, inspections, and process improvement models including SEI CMM and SPICE.",
        },
        {
          name: "Individual Project (CO7201)",
          credits: 60,
          grade: "A (72.24%)",
          description:
            "Independent research project demonstrating advanced knowledge and skills acquired throughout the program.",
        },
      ],
      technologies: [
        "Apache Spark",
        "scikit-learn",
        "Hadoop",
        "MapReduce",
        "Java Servlets",
        "JavaScript",
        "C++",
        "UML",
        "XML",
        "Cloud Computing",
        "Web Services",
      ],
      achievements: [
        "Overall Classification: Distinction",
        "Strong performance across all advanced modules",
        "Comprehensive individual project completion",
        "Advanced expertise in big data and cloud computing",
      ],
    },
  },
  {
    id: "ktu-btech",
    institution: "APJ Abdul Kalam Technological University",
    degree: "B.Tech Computer Science and Engineering",
    duration: "July 2019 - Jun 2023",
    location: "Kerala, India",
    grade: "8.5 CGPA (First Class with Distinction)",
    description: "Bachelor of Technology in Computer Science and Engineering",
    details: {
      overview:
        "Comprehensive 4-year undergraduate program covering fundamental and advanced computer science concepts, with strong emphasis on practical application and project work.",
      college: "Government Engineering College Sreekrishnapuram",
      registerNumber: "PKD19CS031",
      academicPerformance: {
        overallCGPA: "8.5 out of 10.0",
        classification: "First Class with Distinction",
        peakSGPA: "8.97 (Seventh Semester)",
        consistentPerformance:
          "Strong academic performance across all 8 semesters",
      },
      coreSkills: [
        {
          category: "Programming Languages",
          skills: [
            "C Programming",
            "Java (OOP)",
            "Python",
            "R",
            "JavaScript",
            "Assembly Language",
          ],
        },
        {
          category: "CS Fundamentals",
          skills: [
            "Data Structures & Algorithms",
            "Computer Architecture",
            "Operating Systems",
            "DBMS",
            "Computer Networks",
            "System Software",
          ],
        },
        {
          category: "Advanced Technologies",
          skills: [
            "Artificial Intelligence",
            "Machine Learning",
            "Deep Learning",
            "Data Mining",
            "Blockchain",
            "Distributed Computing",
          ],
        },
        {
          category: "Mathematical Foundation",
          skills: [
            "Linear Algebra",
            "Discrete Mathematics",
            "Graph Theory",
            "Formal Languages & Automata",
          ],
        },
      ],
      laboratoryExperience: [
        "Programming Labs (C, Java)",
        "Digital Electronics Lab",
        "Microprocessors Lab",
        "Database Management Lab",
        "Networking Lab",
        "Compiler Lab",
        "System Software Lab",
      ],
      projectWork: [
        "Mini Project (Semester 6) - Grade: A+",
        "Major Project Phase I (Semester 7) - Grade: S",
        "Major Project Phase II (Semester 8) - Grade: B+",
        "Technical Seminars and Comprehensive Course Work",
      ],
      achievements: [
        "CGPA 8.5 with First Class with Distinction",
        "Excellent performance in AI/ML subjects (A+ grades)",
        "Strong foundation in computer science fundamentals",
        "Comprehensive practical experience through lab work",
      ],
    },
  },
];

export const certificationData: Certification[] = [
  {
    id: "aws-cloud-practitioner",
    title: "AWS Certified Cloud Practitioner",
    description:
      "Earned the AWS Certified Cloud Practitioner certification, which validates my understanding of AWS Cloud concepts, services, and terminology.",
    issuer: "Amazon Web Services (AWS)",
    badgeUrl:
      "https://www.credly.com/badges/625f06e2-9e95-4c65-8178-9296e4ba2f71/public_url",
    certificateUrl: "/AWSCertifiedCloudPractitionerCertificate.pdf",
  },
];

export const hackathonData: Hackathon[] = [
  {
    id: "ibm-cic-hackathon",
    title: "IBM CIC Hackathon: Finalist",
    project: "Wise Wallet",
    description:
      "Designed and engineered an innovative receipt analysis application that extracts text from user-uploaded receipts using OCR technology, leveraging a fine-tuned AI model to provide personalized suggestions and feedback.",
    issuer: "IBM",
    badgeUrl:
      "https://www.credly.com/badges/8ff75b39-37e4-44ff-b677-28c4b79f3795/public_url",
    certificateUrl: "/MohammedRishinPoolat.png",
  },
];
