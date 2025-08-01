// Common interfaces
export interface DateRange {
  start: string;
  end: string;
}

export interface Link {
  url: string;
  label: string;
}

export interface TechStack {
  category: string;
  technologies: string[];
}

export interface Achievement {
  metric: string;
  description: string;
}

// Project-related interfaces
export interface ProjectFeature {
  title: string;
  description: string;
  details: string[];
}

export interface ProjectArchitecture {
  backend: string[];
  frontend: string[];
  database: string[];
  deployment: string[];
}

export interface Project {
  id: string;
  title: string;
  shortDescription?: string;
  fullDescription?: string;
  description?: string; // backward compatibility
  githubUrl?: string;
  liveUrl?: string;
  technologies?: string[];
  techStack?: TechStack[] | string[]; // flexible type
  features?: ProjectFeature[] | string[];
  architecture?: ProjectArchitecture;
  achievements?: Achievement[] | string[];
  challenges?: string[];
  solutions?: string[];
  learnings?: string[];
  category?: 'full-stack' | 'ai-ml' | 'web-scraping' | 'mobile' | 'cli-tool' | 'e-commerce' | 'social' | 'computer-vision' | 'other';
  complexity?: 'beginner' | 'intermediate' | 'advanced' | 'expert';
  imageUrl?: string;
  status?: 'completed' | 'in-progress' | 'planned';
}

// Experience interfaces
export interface ExperienceProject {
  name: string;
  description: string;
  technologies: string[];
  achievements: Achievement[];
  impact: string[];
}

export interface Experience {
  id: string;
  company: string;
  position?: string;
  title?: string; // backward compatibility
  location: string;
  startDate?: string;
  endDate?: string;
  duration?: string; // backward compatibility
  companyDescription?: string;
  companyWebsite?: string;
  projects?: ExperienceProject[];
  technologies?: string[];
  achievements?: Achievement[];
  responsibilities: string[];
  impact?: string[];
  skills?: string[];
}

// Education interfaces
export interface CourseModule {
  code: string;
  name: string;
  credits: number;
  grade: string;
  percentage?: number;
  description?: string;
}

export interface Semester {
  number: number;
  sgpa: number;
  modules: CourseModule[];
}

export interface Education {
  id: string;
  degree: string;
  institution: string;
  university?: string;
  location: string;
  startDate?: string;
  endDate?: string;
  duration?: string; // backward compatibility
  cgpa?: number;
  classification?: string;
  semesters?: Semester[];
  coreSkills?: string[];
  projects?: string[];
  achievements?: string[];
  registrationNumber?: string;
}

// Certification interfaces
export interface CertificationDomain {
  name: string;
  percentage: number;
  performance: 'exceeds' | 'meets' | 'needs-improvement';
  description: string;
}

export interface Certification {
  id: string;
  name?: string;
  title?: string; // backward compatibility
  description?: string; // backward compatibility
  issuer: string;
  issueDate?: string;
  expirationDate?: string;
  score?: number;
  maxScore?: number;
  credentialId?: string;
  verificationUrl?: string;
  domains?: CertificationDomain[];
  competencies?: string[];
  benefits?: string[];
  status?: 'active' | 'expired';
  badgeUrl?: string;
  certificateUrl?: string; // backward compatibility
}

// Hackathon interfaces
export interface HackathonProject {
  name: string;
  description: string;
  liveUrl?: string;
  features: string[];
  technologies: string[];
  impact: string[];
}

export interface Hackathon {
  id: string;
  name?: string;
  title?: string; // backward compatibility
  organizer?: string;
  issuer?: string; // backward compatibility
  date?: string;
  location?: string;
  achievement?: string;
  project?: HackathonProject | string; // flexible type
  description?: string; // backward compatibility
  teamSize?: number;
  totalTeams?: number;
  skills?: string[];
  recognition?: string[];
  badgeUrl?: string; // backward compatibility
  certificateUrl?: string; // backward compatibility
  badgeInfo?: {
    name: string;
    issuer: string;
    level: string;
    verificationUrl: string;
  };
}

// Portfolio summary interface
export interface PortfolioData {
  projects: Project[];
  experience: Experience[];
  education: Education[];
  certifications: Certification[];
  hackathons: Hackathon[];
}