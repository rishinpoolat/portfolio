import React from 'react';
import { Project } from '../types/portfolio';
import './ProjectModal.css';

interface ProjectModalProps {
  project: Project;
  onClose: () => void;
}

const ProjectModal: React.FC<ProjectModalProps> = ({ project, onClose }) => {
  return (
    <div className="modal-overlay" onClick={onClose}>
      <div className="modal-content" onClick={(e) => e.stopPropagation()}>
        <button className="modal-close" onClick={onClose} aria-label="Close modal">
          <i className="fas fa-times"></i>
        </button>
        
        <div className="modal-header">
          <h2>{project.title}</h2>
          <div className="modal-links">
            {project.githubUrl && (
              <a
                href={project.githubUrl}
                target="_blank"
                rel="noopener noreferrer"
                className="modal-link"
              >
                <i className="fab fa-github"></i> GitHub
              </a>
            )}
            {project.liveUrl && (
              <a
                href={project.liveUrl}
                target="_blank"
                rel="noopener noreferrer"
                className="modal-link"
              >
                <i className="fas fa-external-link-alt"></i> Live Demo
              </a>
            )}
          </div>
        </div>

        <div className="modal-body">
          <div className="modal-section">
            <h3>Overview</h3>
            <p>{project.fullDescription || (project as any).description}</p>
          </div>

          <div className="modal-section">
            <h3>Tech Stack</h3>
            <div className="tech-tags-modal">
              {(project.techStack || (project as any).techStack || []).map((tech: any, index: number) => (
                <span key={index} className="tech-tag-modal">{tech}</span>
              ))}
            </div>
          </div>

          {project.features && project.features.length > 0 && (
            <div className="modal-section">
              <h3>Key Features</h3>
              <ul className="feature-list">
                {project.features.map((feature, index) => (
                  <li key={index}>
                    {typeof feature === 'string' ? feature : feature.title}
                  </li>
                ))}
              </ul>
            </div>
          )}

          {project.challenges && project.challenges.length > 0 && (
            <div className="modal-section">
              <h3>Technical Challenges</h3>
              <ul className="challenge-list">
                {project.challenges.map((challenge, index) => (
                  <li key={index}>{challenge}</li>
                ))}
              </ul>
            </div>
          )}

          {project.achievements && project.achievements.length > 0 && (
            <div className="modal-section">
              <h3>Achievements</h3>
              <ul className="achievement-list">
                {project.achievements.map((achievement, index) => (
                  <li key={index}>
                    {typeof achievement === 'string' ? achievement : `${achievement.metric}: ${achievement.description}`}
                  </li>
                ))}
              </ul>
            </div>
          )}
        </div>
      </div>
    </div>
  );
};

export default ProjectModal;