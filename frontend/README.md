# Portfolio Frontend

A modern React-based frontend for Mohammed Rishin's portfolio, featuring a responsive design that matches the original portfolio website with enhanced interactive elements.

## Features

- **Responsive Design**: Mobile-first approach with breakpoints for tablets and desktops
- **Project Showcase**: Interactive project cards with detailed modal dialogs
- **Dark Theme**: Beautiful dark theme with red accent colors (#f7564a)
- **Interactive Timeline**: Horizontal timeline showing education and experience
- **Modal System**: Click-to-expand project details with comprehensive information
- **Modern Typography**: Uses Space Grotesk font family for consistent branding
- **Smooth Animations**: Hover effects and transitions for enhanced user experience

## Tech Stack

- **React 18** with TypeScript
- **React Icons** for consistent iconography
- **Axios** for API communication (future backend integration)
- **CSS3** with modern features (Grid, Flexbox, Animations)
- **Mobile-first responsive design**

## Getting Started

### Prerequisites
- Node.js (v16 or higher)
- npm or yarn

### Installation

1. Install dependencies:
```bash
npm install
```

2. Start the development server:
```bash
npm start
```

3. Open [http://localhost:3000](http://localhost:3000) to view it in the browser.

### Build for Production

```bash
npm run build
```

## Project Structure

```
frontend/
├── src/
│   ├── components/          # React components
│   ├── data/               # Portfolio data
│   ├── services/           # API services
│   └── styles/             # CSS files
└── public/                 # Static assets
```

## Key Components

### Header
- Personal introduction and bio
- Social media links (LinkedIn, GitHub, Email)
- Resume download button

### Project Cards
- Interactive cards with hover effects
- Click-to-expand modal dialogs
- Technology tags and external links

### Timeline
- Responsive timeline (horizontal/vertical)
- Education and experience entries
- Smooth animations

## Design Features

### Color Scheme
- **Primary**: Black background (#000000)
- **Accent**: Red (#f7564a)
- **Text**: White (#ffffff) and Light Gray (#c2c2c2)

### Responsive Breakpoints
- Mobile: < 768px
- Tablet: 768px - 1023px
- Desktop: ≥ 1024px

## Available Scripts

### `npm start`
Runs the app in development mode at [http://localhost:3000](http://localhost:3000)

### `npm test`
Launches the test runner in interactive watch mode

### `npm run build`
Builds the app for production to the `build` folder

## Environment Variables

Create a `.env` file:
```env
REACT_APP_API_URL=http://localhost:8000/api/v1
```

## Future Enhancements

- Search functionality
- Theme switching
- Performance optimization
- Enhanced accessibility
- Internationalization

## Learn More

- [Create React App documentation](https://facebook.github.io/create-react-app/docs/getting-started)
- [React documentation](https://reactjs.org/)
