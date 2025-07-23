# Penply - Social Collaboration Platform


## Overview

Penply is a sophisticated full-stack social collaboration platform designed to revolutionize team productivity by consolidating multiple workspace tools into a single, unified solution. This modern web application enables teams to create collaborative "rooms" where members can engage in real-time chat, share notes, schedule events, and manage files - all within an intuitive, seamless interface.

## 🎯 Mission & Vision

Penply addresses the common challenge of tool fragmentation in modern workplaces, where teams juggle multiple applications for communication, note-taking, file sharing, and scheduling. By providing a comprehensive collaboration ecosystem, Penply eliminates context switching and improves team productivity through integrated workflows.

## 🚀 Key Features

### Room-Based Collaboration
- **Collaborative Workspaces**: Create dedicated rooms for projects, teams, or topics
- **Flexible Membership**: Invite users via email with role-based access control
- **Room Management**: Owners can manage members, settings, and room lifecycle
- **Access Control**: Granular permissions for room owners and members

### Real-Time Communication
- **Live Chat**: Instant messaging within rooms using WebSocket technology
- **Message Persistence**: Complete chat history with searchable message archives
- **User Presence**: Real-time indicators showing who's online and active
- **Room Isolation**: Messages are scoped to specific rooms for focused discussions

### Intelligent Note Management
- **Rich Text Notes**: Create and edit notes with formatting support
- **Collaborative Editing**: Share notes within rooms for team collaboration
- **Personal Notes**: Private notes for individual organization
- **Note Organization**: Structured note management with room-based categorization

### Integrated Calendar System
- **Event Scheduling**: Create events with precise start and end times
- **Calendar Views**: Weekly calendar interface with intuitive navigation
- **Meeting Integration**: Support for meeting links and virtual event coordination
- **Conflict Detection**: Smart scheduling to prevent overlapping events

### Secure File Management
- **Cloud Storage**: AWS S3 integration for reliable file storage and retrieval
- **File Sharing**: Upload and share files within room contexts
- **Storage Management**: 100MB per room limit with usage tracking
- **Download Control**: Secure file access with permission validation

### Enterprise-Grade Authentication
- **Multiple Auth Methods**: Google OAuth and traditional email/password registration
- **Multi-Factor Authentication**: TOTP-based OTP system for enhanced security
- **Session Management**: JWT-based authentication with refresh token support
- **Password Security**: Comprehensive password reset and recovery workflows

## 🛠 Technology Stack

### Backend Architecture
- **Runtime Environment**: Node.js with ES modules for modern JavaScript support
- **Web Framework**: Express.js with RESTful API design patterns
- **Database**: PostgreSQL with Prisma ORM for type-safe database operations
- **Real-Time Engine**: Socket.IO for bidirectional WebSocket communication
- **Authentication**: JWT tokens with Google OAuth and Speakeasy 2FA integration
- **File Storage**: AWS S3 with Multer for multipart file uploads
- **Email Service**: Nodemailer with EJS templating for transactional emails
- **Background Jobs**: BullMQ for asynchronous task processing
- **Security**: Helmet for HTTP headers, bcrypt for password hashing
- **Validation**: Joi schema validation for request data integrity

### Frontend Architecture
- **Framework**: React 18 with modern hooks and functional components
- **Build Tool**: Vite for fast development and optimized production builds
- **State Management**: Redux Toolkit for predictable state management
- **Routing**: React Router DOM for client-side navigation
- **Styling**: Tailwind CSS for utility-first responsive design
- **Animations**: Framer Motion for smooth UI animations and transitions
- **HTTP Client**: Axios with interceptors for API communication
- **Real-Time**: Socket.IO client for live chat functionality
- **UI Components**: Custom component library with React Icons
- **Authentication**: @react-oauth/google for OAuth integration
- **Notifications**: React Toastify for user feedback and alerts

## 📁 Project Architecture

### Backend Structure
```
streamlined_backend/
├── app.js                      # Express application configuration
├── bin/
│   └── www.js                  # Server entry point with Socket.IO setup
├── controllers/                # Request handlers and business logic
│   ├── authController.js       # Authentication operations
│   ├── userController.js       # User profile management
│   ├── roomController.js       # Room CRUD operations
│   ├── chatController.js       # Real-time chat handling
│   ├── noteController.js       # Note management
│   ├── eventController.js      # Calendar event operations
│   ├── fileController.js       # File upload/download
│   └── tokenController.js      # JWT token management
├── services/                   # Business logic abstraction
│   ├── user.services.js        # User-related operations
│   ├── room.services.js        # Room management logic
│   ├── chat.services.js        # Chat functionality
│   ├── note.services.js        # Note operations
│   ├── event.services.js       # Event scheduling
│   ├── file.services.js        # File management
│   ├── token.services.js       # Token handling
│   ├── mfa.services.js         # Multi-factor authentication
│   └── activity.services.js    # User activity tracking
├── routes/                     # API route definitions
│   ├── index.js               # Route aggregation
│   ├── authRoutes.js          # Authentication endpoints
│   ├── roomRoute.js           # Room management
│   ├── chatRoute.js           # Chat endpoints
│   ├── noteRoute.js           # Note operations
│   ├── eventRoute.js          # Calendar events
│   └── fileRoute.js           # File operations
├── middlewares/               # Request processing middleware
│   ├── authMiddleware.js      # JWT authentication
│   ├── tokenValidation.js    # Token validation
│   ├── userValidation.js     # User data validation
│   └── schemaValidation.js   # Joi schema validation
├── utils/                     # Utility functions
│   ├── jwt.js                # JWT token utilities
│   ├── email.js              # Email service
│   ├── error.js              # Error handling
│   ├── constants.js          # Application constants
│   ├── bullmq.js             # Queue management
│   ├── emailTemplate.js      # Email templates
│   └── validationSchema.js   # Validation schemas
├── model/
│   └── setupDynamoDB.js       # Database configuration
├── prisma/
│   └── schema.prisma          # Database schema definition
├── views/                     # Email templates
│   ├── invite.ejs            # Room invitation template
│   ├── otp.ejs               # OTP verification template
│   └── resetPassword.ejs     # Password reset template
├── Dockerfile                 # Container configuration
└── package.json              # Dependencies and scripts
```

### Frontend Structure
```
streamlined_frontend/
├── src/
│   ├── components/            # Reusable UI components
│   │   ├── Layout.jsx         # Application layout wrapper
│   │   ├── LoadingScreen.jsx  # Loading state component
│   │   ├── Login.jsx          # Authentication component
│   │   ├── Sidebar.jsx        # Navigation sidebar
│   │   ├── calendar/          # Calendar components
│   │   │   ├── Calendar.jsx   # Main calendar view
│   │   │   └── RoomCalendar.jsx # Room-specific calendar
│   │   ├── chat/
│   │   │   └── Chat.jsx       # Real-time chat interface
│   │   ├── files/
│   │   │   └── Files.jsx      # File management interface
│   │   ├── landing/           # Landing page components
│   │   │   ├── Hero.jsx       # Hero section
│   │   │   ├── Features.jsx   # Features showcase
│   │   │   ├── NavBar.jsx     # Navigation bar
│   │   │   ├── Cta.jsx        # Call-to-action
│   │   │   └── Statement.jsx  # Value proposition
│   │   ├── notes/             # Note management
│   │   │   ├── Notes.jsx      # Notes list view
│   │   │   └── note/
│   │   │       └── Note.jsx   # Individual note component
│   │   ├── rooms/             # Room management
│   │   │   ├── Rooms.jsx      # Rooms list view
│   │   │   └── room/
│   │   │       └── Room.jsx   # Individual room component
│   │   └── roomdetails/
│   │       └── RoomDetails.jsx # Room information panel
│   ├── pages/                 # Route components
│   │   ├── Landing.jsx        # Landing page
│   │   ├── Dashboard.jsx      # Main dashboard
│   │   ├── Room.jsx           # Room detail page
│   │   └── NoteFound.jsx      # 404 page for notes
│   ├── features/              # Redux slices
│   │   ├── auth/
│   │   │   └── authSlice.js   # Authentication state
│   │   ├── notes/
│   │   │   └── notesSlice.js  # Notes state management
│   │   └── room/
│   │       └── roomSlice.js   # Room state management
│   ├── api/                   # API service functions
│   │   ├── chat.js           # Chat API calls
│   │   ├── notes.js          # Notes API calls
│   │   └── todos.js          # Todo API calls
│   ├── utils/                 # Utility functions
│   │   ├── axios.js          # Axios configuration
│   │   ├── constants.js      # Frontend constants
│   │   └── formatDate.js     # Date formatting utilities
│   ├── App.jsx               # Main application component
│   ├── main.jsx              # Application entry point
│   ├── store.js              # Redux store configuration
│   └── index.css             # Global styles
├── public/                    # Static assets
│   ├── icon.png              # Application icon
│   ├── iconw.png             # White icon variant
│   └── computer_man.svg      # Illustration asset
├── index.html                # HTML template
├── package.json              # Dependencies and scripts
├── tailwind.config.js        # Tailwind CSS configuration
├── vite.config.js            # Vite build configuration
└── postcss.config.js         # PostCSS configuration
```

## 🗄️ Database Design

### Core Data Models (Prisma Schema)

#### User Model
```prisma
model User {
  id              Int           @id @default(autoincrement())
  name            String?
  email           String        @unique
  password        String?
  picture         String?
  isGoogleAuth    Boolean       @default(false)
  isVerified      Boolean       @default(false)
  createdAt       DateTime      @default(now())
  updatedAt       DateTime      @updatedAt
  
  // Relationships
  ownedRooms      Room[]        @relation("RoomOwner")
  roomMemberships RoomUser[]
  notes           Note[]
  events          Event[]
  invitedUsers    InvitedUser[]
  blacklistedTokens BlackList[]
}
```

#### Room Model
```prisma
model Room {
  id          Int         @id @default(autoincrement())
  name        String
  description String?
  ownerId     Int
  createdAt   DateTime    @default(now())
  updatedAt   DateTime    @updatedAt
  
  // Relationships
  owner       User        @relation("RoomOwner", fields: [ownerId], references: [id])
  members     RoomUser[]
  notes       Note[]
  events      Event[]
  files       File[]
  invitations InvitedUser[]
}
```

#### RoomUser Junction Model
```prisma
model RoomUser {
  id       Int      @id @default(autoincrement())
  userId   Int
  roomId   Int
  joinedAt DateTime @default(now())
  
  // Relationships
  user     User     @relation(fields: [userId], references: [id])
  room     Room     @relation(fields: [roomId], references: [id])
  
  @@unique([userId, roomId])
}
```

### Additional Models
- **Note**: Text content with room association and ownership
- **Event**: Calendar events with scheduling information
- **File**: File metadata with S3 storage references
- **InvitedUser**: Pending room invitations
- **BlackList**: JWT token revocation for secure logout

## 🔐 Authentication & Security

### Multi-Layer Security Architecture

#### Authentication Methods
1. **Traditional Registration**: Email/password with OTP verification
2. **Google OAuth**: Single sign-on with Google accounts
3. **Multi-Factor Authentication**: TOTP-based OTP using Speakeasy
4. **Session Management**: JWT access tokens with refresh token rotation

#### Security Middleware Stack
```javascript
// Authentication middleware
const authMiddleware = {
  verifyToken: async (req, res, next) => {
    // JWT token verification
    // User authentication check
    // Request context enrichment
  },
  
  validateRoomAccess: async (req, res, next) => {
    // Room membership validation
    // Permission level verification
    // Access control enforcement
  }
}
```

#### Data Protection
- **Password Hashing**: bcrypt with salt rounds for secure password storage
- **Token Management**: JWT with configurable expiration and refresh mechanisms
- **Input Validation**: Joi schema validation for all API endpoints
- **CORS Configuration**: Controlled cross-origin resource sharing
- **Security Headers**: Helmet.js for HTTP security headers

## 🌐 API Architecture

### RESTful Endpoint Structure

#### Authentication Endpoints
```
POST   /auth/signup          # User registration with OTP
POST   /auth/google          # Google OAuth authentication
POST   /auth/login           # Standard email/password login
POST   /auth/verify          # OTP verification for 2FA
POST   /auth/forgot-password # Password reset initialization
POST   /auth/reset-password  # Password reset completion
POST   /auth/logout          # Session termination
GET    /auth/refresh         # Access token refresh
```

#### Protected Resource Endpoints
```
# Room Management
GET    /rooms                # List user's rooms
POST   /rooms                # Create new room
GET    /rooms/:id            # Get room details
PUT    /rooms/:id            # Update room information
DELETE /rooms/:id            # Delete room (owner only)
POST   /rooms/:id/invite     # Invite users to room
POST   /rooms/:id/join       # Join room via invitation

# Notes Management
GET    /rooms/:id/notes      # List room notes
POST   /rooms/:id/notes      # Create new note
GET    /notes/:id            # Get specific note
PUT    /notes/:id            # Update note content
DELETE /notes/:id            # Delete note (owner only)

# Real-time Chat
GET    /rooms/:id/chat       # Get chat history
POST   /rooms/:id/chat       # Send message (via Socket.IO)

# Calendar Events
GET    /rooms/:id/events     # List room events
POST   /rooms/:id/events     # Create new event
GET    /events/:id           # Get event details
PUT    /events/:id           # Update event
DELETE /events/:id           # Delete event (owner only)

# File Management
GET    /rooms/:id/files      # List room files
POST   /rooms/:id/files      # Upload file
GET    /files/:id/download   # Download file
DELETE /files/:id            # Delete file (owner only)

# User Profile
GET    /me                   # Get user profile
PUT    /me                   # Update user profile
```

## ⚡ Real-Time Features

### Socket.IO Integration
```javascript
// Server-side Socket.IO configuration
io.on('connection', (socket) => {
  // User authentication
  socket.on('authenticate', (token) => {
    // JWT verification and user context
  });
  
  // Room-based messaging
  socket.on('join-room', (roomId) => {
    socket.join(`room-${roomId}`);
  });
  
  socket.on('send-message', (data) => {
    // Message validation and persistence
    // Room-wide message broadcast
    io.to(`room-${data.roomId}`).emit('new-message', message);
  });
  
  // User presence tracking
  socket.on('user-typing', (data) => {
    socket.to(`room-${data.roomId}`).emit('user-typing', data);
  });
});
```

### Frontend Real-Time Integration
```javascript
// React Socket.IO integration
const useSocket = (roomId) => {
  const socket = useRef();
  
  useEffect(() => {
    socket.current = io(API_URL, {
      auth: { token: localStorage.getItem('accessToken') }
    });
    
    socket.current.emit('join-room', roomId);
    
    socket.current.on('new-message', (message) => {
      // Update chat state
      dispatch(addMessage(message));
    });
    
    return () => socket.current.disconnect();
  }, [roomId]);
};
```

## 🚀 Installation & Deployment

### Development Setup

#### Prerequisites
- Node.js 18+ and npm/yarn
- PostgreSQL database
- AWS S3 bucket for file storage
- Gmail account for email services (or alternative SMTP)

#### Backend Installation
```bash
# Navigate to backend directory
cd streamlined_backend

# Install dependencies
npm install

# Set up environment variables
cp .env.example .env
# Configure DATABASE_URL, JWT_SECRET, AWS credentials, etc.

# Initialize database
npx prisma migrate dev
npx prisma generate

# Start development server
npm run dev
```

#### Frontend Installation
```bash
# Navigate to frontend directory
cd streamlined_frontend

# Install dependencies
npm install

# Set up environment variables
cp .env.example .env
# Configure VITE_API_URL, VITE_GOOGLE_CLIENT_ID

# Start development server
npm run dev
```

### Production Deployment

#### Docker Deployment
```bash
# Build and run backend container
cd streamlined_backend
docker build -t penply-backend .
docker run -p 8080:8080 --env-file .env penply-backend

# Frontend build for production
cd streamlined_frontend
npm run build
# Deploy dist/ directory to static hosting (Vercel, Netlify, etc.)
```

#### Environment Variables

##### Backend Configuration
```env
# Database
DATABASE_URL_DEV=postgresql://user:password@localhost:5432/penply

# Authentication
JWT_SECRET=your-jwt-secret-key
JWT_REFRESH_SECRET=your-refresh-secret-key
GOOGLE_CLIENT_ID=your-google-oauth-client-id
GOOGLE_CLIENT_SECRET=your-google-oauth-client-secret

# AWS S3
AWS_ACCESS_KEY_ID=your-aws-access-key
AWS_SECRET_ACCESS_KEY=your-aws-secret-key
AWS_S3_BUCKET=your-s3-bucket-name
AWS_REGION=us-east-1

# Email Service
SMTP_HOST=smtp.gmail.com
SMTP_PORT=587
SMTP_USER=your-email@gmail.com
SMTP_PASS=your-app-password

# Application
PORT=8080
NODE_ENV=production
FRONTEND_URL=https://yourapp.com
```

##### Frontend Configuration
```env
VITE_API_URL=https://api.yourapp.com
VITE_GOOGLE_CLIENT_ID=your-google-client-id
VITE_SOCKET_URL=https://api.yourapp.com
```

## 📱 Usage Examples

### Creating a Collaboration Room
```javascript
// Frontend: Create room workflow
const createRoom = async (roomData) => {
  try {
    const response = await axios.post('/rooms', {
      name: roomData.name,
      description: roomData.description
    });
    
    // Navigate to new room
    navigate(`/room/${response.data.id}`);
  } catch (error) {
    toast.error('Failed to create room');
  }
};
```

### Real-Time Chat Integration
```javascript
// Chat component with real-time messaging
const ChatComponent = ({ roomId }) => {
  const [messages, setMessages] = useState([]);
  const [newMessage, setNewMessage] = useState('');
  
  useEffect(() => {
    socket.emit('join-room', roomId);
    
    socket.on('new-message', (message) => {
      setMessages(prev => [...prev, message]);
    });
    
    return () => socket.off('new-message');
  }, [roomId]);
  
  const sendMessage = () => {
    socket.emit('send-message', {
      roomId,
      content: newMessage,
      userId: user.id
    });
    setNewMessage('');
  };
};
```

### File Upload with Progress Tracking
```javascript
// File upload with progress feedback
const uploadFile = async (file, roomId) => {
  const formData = new FormData();
  formData.append('file', file);
  
  try {
    const response = await axios.post(`/rooms/${roomId}/files`, formData, {
      headers: { 'Content-Type': 'multipart/form-data' },
      onUploadProgress: (progressEvent) => {
        const progress = Math.round(
          (progressEvent.loaded * 100) / progressEvent.total
        );
        setUploadProgress(progress);
      }
    });
    
    toast.success('File uploaded successfully');
    return response.data;
  } catch (error) {
    toast.error('Upload failed');
  }
};
```

## 🎯 Advanced Features

### Collaborative Note System
- **Rich Text Editing**: Support for formatted text with markdown compatibility
- **Version History**: Track changes and revisions to collaborative notes
- **Comment System**: Inline comments for collaborative feedback
- **Permission Levels**: Read-only, edit, and admin permissions for notes

### Smart Calendar Integration
- **Recurring Events**: Support for repeating events with flexible patterns
- **Time Zone Support**: Automatic time zone conversion for global teams
- **Meeting Room Integration**: Integration with video conferencing platforms
- **Calendar Sync**: Export to external calendar applications

### Advanced File Management
- **Version Control**: File versioning with rollback capabilities
- **Preview System**: In-browser preview for documents and images
- **Collaborative Editing**: Real-time collaborative document editing
- **Access Analytics**: Track file access and download statistics

### Team Analytics
- **Activity Dashboard**: Team activity and engagement metrics
- **Usage Statistics**: Room and feature usage analytics
- **Performance Insights**: System performance and user experience metrics
- **Export Capabilities**: Data export for external analysis

## 🔮 Future Enhancements

### Planned Features
1. **Mobile Applications**: Native iOS and Android apps with full feature parity
2. **Advanced Integrations**: Slack, Microsoft Teams, Google Workspace integration
3. **AI-Powered Features**: Smart meeting summaries, content suggestions
4. **Enterprise Features**: SSO, advanced security, audit logs
5. **Workflow Automation**: Custom workflows and automation rules
6. **Advanced Search**: Full-text search across all content types
7. **Whiteboard Integration**: Collaborative visual workspace tools
8. **Voice/Video Calls**: Integrated video conferencing capabilities

### Technical Roadmap
- **Microservices Architecture**: Service decomposition for better scalability
- **GraphQL API**: More efficient data fetching and real-time subscriptions
- **Progressive Web App**: Enhanced mobile experience with offline capabilities
- **Advanced Caching**: Redis integration for improved performance
- **Monitoring & Analytics**: Comprehensive application monitoring and logging

## 🤝 Contributing

### Development Guidelines
- **Code Style**: ESLint and Prettier configuration for consistent formatting
- **Testing**: Jest for backend testing, React Testing Library for frontend
- **Documentation**: Comprehensive API documentation with OpenAPI/Swagger
- **Git Workflow**: Feature branches with pull request reviews
- **Security**: Regular security audits and dependency updates

### Architecture Principles
- **Modularity**: Clean separation of concerns with modular architecture
- **Scalability**: Designed for horizontal scaling and high availability
- **Security**: Security-first approach with comprehensive protection measures
- **Performance**: Optimized for speed and efficient resource utilization
- **User Experience**: Intuitive interface with accessibility considerations

## 📊 Technical Specifications

- **Backend Language**: JavaScript (Node.js ES modules)
- **Frontend Language**: JavaScript (React 18)
- **Database**: PostgreSQL with Prisma ORM
- **Real-Time**: Socket.IO for WebSocket communication
- **File Storage**: AWS S3 with CloudFront CDN
- **Authentication**: JWT with OAuth2 integration
- **Deployment**: Docker containers with cloud platform support
- **Performance**: Optimized for concurrent users and real-time interactions

Penply represents a comprehensive solution for modern team collaboration, combining the best practices of full-stack web development with innovative features designed to enhance productivity and team communication. The platform demonstrates advanced technical implementation while maintaining a focus on user experience and security.