import React from 'react';
import { Project } from '../types/portfolio';
import './ProjectCard.css';

// Re-export for backward compatibility
export type { Project } from '../types/portfolio';

interface ProjectCardProps {
  project: Project;
  onClick: () => void;
}

const ProjectCard: React.FC<ProjectCardProps> = ({ project, onClick }) => {
  const handleCardClick = (e: React.MouseEvent) => {
    if (e.target === e.currentTarget || !(e.target as HTMLElement).closest('a')) {
      onClick();
    }
  };

  return (
    <div className="project-card" onClick={handleCardClick}>
      <h3>{project.title}</h3>
      <p className="project-description">
        {project.shortDescription || (project as any).description || project.fullDescription}
      </p>
      <div className="tech-stack">
        <strong>Tech Stack:</strong>
        <div className="tech-tags">
          {(project.technologies || (project as any).techStack || []).map((tech: any, index: number) => (
            <span key={index} className="tech-tag">
              {typeof tech === 'string' ? tech : tech}
            </span>
          ))}
        </div>
      </div>
      <div className="project-links">
        {project.githubUrl && (
          <a
            href={project.githubUrl}
            target="_blank"
            rel="noopener noreferrer"
            className="project-link"
            onClick={(e) => e.stopPropagation()}
          >
            <i className="fab fa-github"></i> GitHub
          </a>
        )}
        {project.liveUrl && (
          <a
            href={project.liveUrl}
            target="_blank"
            rel="noopener noreferrer"
            className="project-link"
            onClick={(e) => e.stopPropagation()}
          >
            <i className="fas fa-external-link-alt"></i> Live Demo
          </a>
        )}
      </div>
      <div className="click-hint">Click to view details</div>
    </div>
  );
};

export default ProjectCard;