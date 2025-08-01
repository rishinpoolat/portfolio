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
              {(project.technologies || project.techStack || []).map((tech: any, index: number) => {
                if (typeof tech === 'string') {
                  return (
                    <span key={index} className="tech-tag-modal">{tech}</span>
                  );
                } else if (tech && typeof tech === 'object' && tech.technologies) {
                  // Handle techStack objects with category and technologies
                  return tech.technologies.map((subTech: string, subIndex: number) => (
                    <span key={`${index}-${subIndex}`} className="tech-tag-modal">{subTech}</span>
                  ));
                }
                return null;
              })}
            </div>
          </div>

          {project.features && project.features.length > 0 && (
            <div className="modal-section">
              <h3>Key Features</h3>
              <div className="features-container">
                {project.features.map((feature, index) => {
                  if (typeof feature === 'string') {
                    return (
                      <div key={index} className="feature-item">
                        <h4>{feature}</h4>
                      </div>
                    );
                  } else if (feature && typeof feature === 'object') {
                    return (
                      <div key={index} className="feature-item">
                        <h4>{feature.title}</h4>
                        {feature.description && (
                          <p className="feature-description">{feature.description}</p>
                        )}
                        {feature.details && feature.details.length > 0 && (
                          <ul className="feature-details">
                            {feature.details.map((detail: string, detailIndex: number) => (
                              <li key={detailIndex}>{detail}</li>
                            ))}
                          </ul>
                        )}
                      </div>
                    );
                  }
                  return null;
                })}
              </div>
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
              <div className="achievements-grid">
                {project.achievements.map((achievement, index) => {
                  if (typeof achievement === 'string') {
                    return (
                      <div key={index} className="achievement-item">
                        <span>{achievement}</span>
                      </div>
                    );
                  } else if (achievement && typeof achievement === 'object') {
                    return (
                      <div key={index} className="achievement-item">
                        <span className="metric">{achievement.metric}</span>
                        <span className="description">{achievement.description}</span>
                      </div>
                    );
                  }
                  return null;
                })}
              </div>
            </div>
          )}
        </div>
      </div>
    </div>
  );
};

export default ProjectModal;