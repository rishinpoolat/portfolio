# SocialApp - Full-Stack Social Media Platform

[GitHub Repository](https://github.com/rishinpoolat/socialapp)

## Overview

SocialApp is a comprehensive full-stack social media platform designed to deliver an engaging and secure social networking experience. Built with modern web technologies, this application provides users with essential social media features including user authentication with OTP verification, real-time posting capabilities, social interactions through likes and comments, and a robust follow system for building social connections.

## 🎯 Mission & Purpose

SocialApp addresses the need for a clean, secure, and feature-rich social media platform that prioritizes user experience and data security. By implementing comprehensive authentication mechanisms and real-time social interactions, the platform provides a solid foundation for modern social networking while maintaining simplicity and ease of use.

## 🚀 Key Features

### Advanced Authentication System
- **Multi-Factor Authentication**: OTP (One-Time Password) verification using Speakeasy for enhanced security
- **Email Verification**: Complete email verification workflow with secure token generation
- **Password Security**: Bcrypt-based password hashing with salt rounds for maximum security
- **Session Management**: JWT-based authentication with secure cookie handling
- **Password Recovery**: Comprehensive forgot password and reset functionality

### Social Networking Core
- **User Profiles**: Comprehensive user profile management with personal information
- **Real-Time Posts**: Create, edit, and share posts with multimedia support
- **Social Interactions**: Like and comment system for engaging content interactions
- **Follow System**: Follow/unfollow functionality to build social connections
- **Activity Feed**: Real-time activity feed showing posts from followed users

### Content Management
- **Media Upload**: Support for image and file uploads with Multer middleware
- **Post Management**: Full CRUD operations for user-generated content
- **Content Moderation**: Built-in mechanisms for content validation and security
- **Responsive Design**: Mobile-first responsive design for cross-device compatibility

### Communication Features
- **Real-Time Notifications**: Live notification system for user interactions
- **Comment Threads**: Hierarchical comment system for detailed discussions
- **User Search**: Advanced search functionality to discover and connect with users
- **Activity Tracking**: Comprehensive activity logging and user engagement metrics

## 🛠 Technology Stack

### Backend Architecture
- **Runtime Environment**: Node.js with Express.js framework for robust server-side operations
- **Database**: PostgreSQL with Sequelize ORM for reliable data persistence and relationships
- **Authentication**: JWT (JSON Web Tokens) for stateless authentication
- **Security**: bcrypt for password hashing, Speakeasy for OTP generation
- **Email Service**: Nodemailer with SMTP integration for transactional emails
- **File Handling**: Multer middleware for multipart/form-data and file uploads
- **Input Validation**: Validator.js for comprehensive input sanitization and validation
- **Process Management**: PM2 for production deployment and process monitoring

### Frontend & View Layer
- **Template Engine**: EJS (Embedded JavaScript) for server-side rendering
- **Styling**: Custom CSS with responsive design principles
- **Interactive Elements**: Client-side JavaScript for dynamic user interactions
- **Form Handling**: Comprehensive form validation and user feedback systems

### Development & DevOps
- **Code Quality**: ESLint with Airbnb configuration for code consistency
- **Code Formatting**: Prettier for automated code formatting
- **Process Management**: Ecosystem configuration for PM2 deployment
- **Environment Management**: dotenv for secure environment variable handling

## 📁 Project Architecture

### Backend Structure
```
socialapp/
├── app.js                          # Express application configuration
├── bin/
│   └── www                         # Server entry point
├── controllers/                    # Business logic controllers
│   ├── userController.js           # User management operations
│   ├── postController.js           # Post CRUD operations
│   └── notificationController.js   # Notification handling
├── models/                         # Database models and configuration
│   ├── index.js                    # Sequelize database connection
│   ├── config.js                   # Database configuration
│   ├── userModel.js                # User data model
│   ├── postModel.js                # Post data model
│   ├── commentModel.js             # Comment data model
│   ├── likeModel.js                # Like interaction model
│   ├── followModel.js              # Follow relationship model
│   ├── notificationModel.js        # Notification data model
│   └── socialapp.sql               # Database schema definition
├── routes/                         # API endpoint definitions
│   ├── index.js                    # Main route handler
│   ├── userRoute.js                # User-related endpoints
│   ├── postRoute.js                # Post management endpoints
│   └── notificationRoute.js        # Notification endpoints
├── middlewares/                    # Request processing middleware
│   ├── authMiddleware.js           # Authentication validation
│   └── multerMiddleware.js         # File upload handling
├── views/                          # EJS templates
│   ├── template.ejs                # Base template layout
│   ├── login.ejs                   # Login page
│   ├── signup.ejs                  # Registration page
│   ├── home.ejs                    # Main dashboard
│   ├── profile.ejs                 # User profile page
│   ├── addPost.ejs                 # Post creation interface
│   ├── explore.ejs                 # Content discovery page
│   ├── search.ejs                  # User search interface
│   ├── followers.ejs               # Followers list view
│   ├── followings.ejs              # Following list view
│   ├── notifications.ejs           # Notifications center
│   ├── forgot.ejs                  # Password reset request
│   ├── reset.ejs                   # Password reset form
│   ├── verifyOtp.ejs               # OTP verification page
│   └── error.ejs                   # Error page template
├── public/                         # Static assets
│   └── stylesheets/
│       ├── style.css               # Main application styles
│       └── error.css               # Error page styles
├── ecosystem.config.js             # PM2 deployment configuration
└── package.json                    # Dependencies and scripts
```

## 🗄️ Database Design

### Core Data Models (Sequelize)

#### User Model
```javascript
const User = sequelize.define("User", {
  id: {
    type: DataTypes.INTEGER,
    autoIncrement: true,
    primaryKey: true,
  },
  name: {
    type: DataTypes.STRING,
    allowNull: false,
  },
  email: {
    type: DataTypes.STRING,
    allowNull: false,
    unique: true,
  },
  password: {
    type: DataTypes.STRING,
    allowNull: false,
  },
  otpSecret: {
    type: DataTypes.STRING,
    allowNull: true,
  },
  isOtpVerified: {
    type: DataTypes.BOOLEAN,
    defaultValue: false,
  }
});
```

#### Post Model
```javascript
const Post = sequelize.define("Post", {
  id: {
    type: DataTypes.INTEGER,
    primaryKey: true,
    autoIncrement: true,
  },
  body: {
    type: DataTypes.TEXT,
  },
  userId: {
    type: DataTypes.INTEGER,
  },
  media: {
    type: DataTypes.BLOB,
  }
});
```

### Relationship Models
- **Comment**: Links users to posts with comment content
- **Like**: Tracks user likes on posts for engagement metrics
- **Follow**: Manages follower-following relationships between users
- **Notification**: Stores user activity notifications and alerts

### Database Schema
The application includes a comprehensive SQL schema (`socialapp.sql`) that defines:
- Primary key relationships and foreign key constraints
- Indexes for optimized query performance  
- Proper data types and validation rules
- Referential integrity for data consistency

## 🔐 Authentication & Security

### Multi-Layer Security Implementation

#### Authentication Flow
1. **User Registration**: Email validation with secure password requirements
2. **OTP Generation**: Speakeasy-based time-based OTP for two-factor authentication
3. **Email Verification**: Secure token-based email verification workflow
4. **Session Management**: JWT-based stateless authentication with secure cookies
5. **Password Recovery**: Comprehensive forgot password and reset functionality

#### Security Measures
```javascript
// Password hashing with bcrypt
const hashPassword = async (password) => {
  const saltRounds = 12;
  return await bcrypt.hash(password, saltRounds);
};

// OTP generation with Speakeasy
const generateOTP = () => {
  const secret = speakeasy.generateSecret({
    name: 'SocialApp',
    length: 32
  });
  return secret;
};

// JWT token generation
const generateToken = (user) => {
  return jwt.sign(
    { userId: user.id, email: user.email },
    process.env.JWT_SECRET,
    { expiresIn: '24h' }
  );
};
```

#### Input Validation & Sanitization
- **Validator.js Integration**: Comprehensive input validation for all user data
- **SQL Injection Prevention**: Parameterized queries with Sequelize ORM
- **XSS Protection**: Input sanitization and output encoding
- **CSRF Protection**: Token-based cross-site request forgery prevention

## 🌐 API Architecture

### RESTful Endpoint Structure

#### Authentication Endpoints
```
POST   /users/signup           # User registration with OTP
POST   /users/verify-otp       # OTP verification for account activation
POST   /users/login            # User authentication
POST   /users/forgot-password  # Password reset initialization  
POST   /users/reset-password   # Password reset completion
POST   /users/logout           # Session termination
```

#### Social Features Endpoints
```
# User Management
GET    /users/profile/:id      # Get user profile information
PUT    /users/profile          # Update user profile
GET    /users/search           # Search users by name/email
GET    /users/followers/:id    # Get user followers list
GET    /users/following/:id    # Get user following list
POST   /users/follow/:id       # Follow a user
POST   /users/unfollow/:id     # Unfollow a user

# Post Management  
GET    /posts                  # Get user timeline posts
POST   /posts                  # Create new post
GET    /posts/:id              # Get specific post details
PUT    /posts/:id              # Update post content
DELETE /posts/:id              # Delete post
POST   /posts/:id/like         # Like/unlike post
POST   /posts/:id/comment      # Add comment to post

# Notifications
GET    /notifications          # Get user notifications
PUT    /notifications/:id/read # Mark notification as read
DELETE /notifications/:id      # Delete notification
```

## 📱 User Interface & Experience

### Server-Side Rendered Views

#### Authentication Interface
- **Login Page**: Clean, responsive login form with validation feedback
- **Registration Page**: Multi-step registration with OTP verification
- **Password Recovery**: User-friendly forgot password and reset workflow
- **OTP Verification**: Secure OTP input interface with resend functionality

#### Main Application Interface
- **Dashboard/Home**: Activity feed with posts from followed users
- **Profile Management**: Comprehensive profile editing and viewing interface
- **Post Creation**: Rich post creation interface with media upload support
- **Social Features**: Follow/unfollow buttons with real-time feedback
- **Search Interface**: Advanced user search with filtering capabilities

#### Navigation & Layout
- **Template System**: Consistent EJS template inheritance for uniform UI
- **Responsive Design**: Mobile-first approach ensuring cross-device compatibility
- **Error Handling**: Comprehensive error pages with user-friendly messages
- **Loading States**: Visual feedback for asynchronous operations

## 🚀 Installation & Development Setup

### Prerequisites
- Node.js 16+ and npm
- PostgreSQL database server
- SMTP email service (Gmail, SendGrid, etc.)
- Code editor with ESLint support

### Installation Steps

#### Environment Setup
```bash
# Clone the repository
git clone <repository-url>
cd socialapp

# Install dependencies
npm install

# Create environment variables file
cp .env.example .env
```

#### Environment Configuration
```env
# Database Configuration
DB_HOST=localhost
DB_NAME=socialapp
DB_USER=your_db_user
DB_PASS=your_db_password
DB_PORT=5432

# JWT Configuration
JWT_SECRET=your-super-secret-jwt-key
JWT_EXPIRES_IN=24h

# Email Service Configuration
SMTP_HOST=smtp.gmail.com
SMTP_PORT=587
SMTP_USER=your-email@gmail.com
SMTP_PASS=your-app-password

# Application Configuration
NODE_ENV=development
PORT=3000
BASE_URL=http://localhost:3000
```

#### Database Setup
```bash
# Create PostgreSQL database
createdb socialapp

# Run database migrations
npm run migrate

# Seed initial data (optional)
npm run seed
```

#### Development Workflow
```bash
# Start development server with nodemon
npm run devstart

# Start production server
npm start

# Run linting
npm run lint

# Format code with Prettier
npm run format
```

## 📊 Features Deep Dive

### User Authentication System
The authentication system implements industry-standard security practices:

- **Multi-Factor Authentication**: Speakeasy-based TOTP for enhanced security
- **Email Verification**: Comprehensive email verification workflow
- **Password Security**: bcrypt hashing with configurable salt rounds
- **Session Management**: JWT tokens with secure cookie handling
- **Account Recovery**: Forgot password functionality with secure token validation

### Social Networking Features
Core social media functionality includes:

- **User Profiles**: Comprehensive profile management with personal information
- **Post System**: Rich text posts with multimedia support and real-time updates
- **Engagement System**: Like and comment functionality for user interactions
- **Follow System**: Bidirectional following relationships with real-time updates
- **Activity Feed**: Personalized timeline showing posts from followed users

### Content Management
Advanced content handling capabilities:

- **Media Upload**: Secure file upload with Multer middleware integration
- **Content Validation**: Server-side validation for all user-generated content
- **Post Management**: Full CRUD operations with proper authorization
- **Search Functionality**: Advanced user search with fuzzy matching
- **Notification System**: Real-time notifications for user interactions

## 🎯 Advanced Features

### Real-Time Notifications
```javascript
// Notification creation and delivery
const createNotification = async (userId, type, content, relatedId) => {
  const notification = await Notification.create({
    userId,
    type,
    content,
    relatedId,
    isRead: false,
    createdAt: new Date()
  });
  
  // Real-time notification delivery via Socket.IO (if implemented)
  // io.to(`user-${userId}`).emit('notification', notification);
  
  return notification;
};
```

### Advanced Search System
- **User Discovery**: Search users by name, email, or username
- **Content Search**: Search through posts and comments
- **Fuzzy Matching**: Intelligent search with typo tolerance
- **Filter Options**: Advanced filtering by date, user, or content type

### Analytics & Insights
- **User Engagement**: Track likes, comments, and follow interactions
- **Content Performance**: Analyze post reach and engagement metrics
- **User Activity**: Monitor user login patterns and activity levels
- **Growth Metrics**: Track user acquisition and retention rates

## 🔧 Configuration & Customization

### Application Configuration
```javascript
// app.js configuration
app.disable("x-powered-by");  // Security enhancement
app.use(logger("dev"));       // Request logging
app.use(express.json());      // JSON parsing
app.use(cookieParser());      // Cookie parsing
app.use(express.static("public"));  // Static file serving
```

### Security Middleware
```javascript
// Authentication middleware
const authMiddleware = (req, res, next) => {
  const token = req.cookies.token || req.headers.authorization;
  
  if (!token) {
    return res.redirect('/users/login');
  }
  
  try {
    const decoded = jwt.verify(token, process.env.JWT_SECRET);
    req.user = decoded;
    next();
  } catch (error) {
    res.clearCookie('token');
    return res.redirect('/users/login');
  }
};
```

### File Upload Configuration
```javascript
// Multer configuration for file uploads
const storage = multer.diskStorage({
  destination: (req, file, cb) => {
    cb(null, 'uploads/');
  },
  filename: (req, file, cb) => {
    const uniqueName = `${Date.now()}-${Math.round(Math.random() * 1E9)}`;
    cb(null, `${uniqueName}${path.extname(file.originalname)}`);
  }
});

const upload = multer({
  storage,
  limits: { fileSize: 5 * 1024 * 1024 }, // 5MB limit
  fileFilter: (req, file, cb) => {
    const allowedTypes = /jpeg|jpg|png|gif/;
    const extname = allowedTypes.test(path.extname(file.originalname).toLowerCase());
    const mimetype = allowedTypes.test(file.mimetype);
    
    if (mimetype && extname) {
      return cb(null, true);
    } else {
      cb(new Error('Only image files are allowed'));
    }
  }
});
```

## 🚀 Deployment & Production

### PM2 Production Configuration
```javascript
// ecosystem.config.js
module.exports = {
  apps: [{
    name: 'socialapp',
    script: './bin/www',
    instances: 'max',
    exec_mode: 'cluster',
    env: {
      NODE_ENV: 'development',
      PORT: 3000
    },
    env_production: {
      NODE_ENV: 'production',
      PORT: 8080
    },
    error_file: './logs/err.log',
    out_file: './logs/out.log',
    log_file: './logs/combined.log',
    time: true
  }]
};
```

### Production Deployment Steps
```bash
# Install PM2 globally
npm install -g pm2

# Start application with PM2
pm2 start ecosystem.config.js --env production

# Monitor application
pm2 monit

# Set up auto-restart on system reboot
pm2 startup
pm2 save
```

### Database Production Setup
- **Connection Pooling**: Configure PostgreSQL connection pooling for high concurrency
- **Indexing Strategy**: Implement proper database indexes for query optimization
- **Backup Strategy**: Set up automated database backups and recovery procedures
- **Performance Monitoring**: Monitor database performance and query execution times

## 🔮 Future Enhancements

### Planned Features
1. **Real-Time Chat**: Direct messaging system between users
2. **Story Feature**: Temporary post sharing with auto-expiration
3. **Group Functionality**: Create and manage user groups and communities
4. **Advanced Media**: Video upload and processing capabilities
5. **Mobile API**: REST API for mobile application development
6. **Content Moderation**: AI-powered content moderation and filtering
7. **Analytics Dashboard**: Comprehensive analytics for users and administrators
8. **Social Login**: Integration with Facebook, Twitter, and other social platforms

### Technical Improvements
- **WebSocket Integration**: Real-time features using Socket.IO
- **Caching Layer**: Redis integration for improved performance
- **CDN Integration**: Content delivery network for media files
- **Microservices Architecture**: Service decomposition for better scalability
- **API Documentation**: Comprehensive API documentation with Swagger/OpenAPI
- **Automated Testing**: Unit and integration testing with Jest and Supertest

## 🤝 Contributing

### Development Guidelines
- **Code Style**: Follow ESLint Airbnb configuration for consistency
- **Git Workflow**: Use feature branches with descriptive commit messages
- **Testing**: Write tests for new features and bug fixes
- **Documentation**: Update documentation for any new features or changes
- **Security**: Follow security best practices and conduct regular security audits

### Architecture Principles
- **MVC Pattern**: Maintain clear separation between models, views, and controllers
- **DRY Principle**: Avoid code duplication through proper abstraction
- **Security First**: Implement security measures from the ground up
- **Scalability**: Design for horizontal scaling and high availability
- **Performance**: Optimize for speed and efficient resource utilization

## 📊 Technical Specifications

- **Backend**: Node.js with Express.js framework
- **Database**: PostgreSQL with Sequelize ORM
- **Authentication**: JWT with multi-factor authentication support
- **File Storage**: Local storage with Multer middleware
- **Template Engine**: EJS for server-side rendering
- **Process Management**: PM2 for production deployment
- **Security**: bcrypt, Speakeasy, and comprehensive input validation
- **Development Tools**: ESLint, Prettier, and nodemon

SocialApp represents a comprehensive social media platform that demonstrates modern web development practices, security implementations, and scalable architecture patterns. The application provides a solid foundation for social networking features while maintaining simplicity and extensibility for future enhancements.