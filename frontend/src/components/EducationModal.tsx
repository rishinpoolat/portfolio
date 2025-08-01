import React from 'react';
import { Education } from '../types/portfolio';
import './EducationModal.css';

interface EducationModalProps {
  education: Education;
  onClose: () => void;
}

const EducationModal: React.FC<EducationModalProps> = ({ education, onClose }) => {
  const handleBackdropClick = (e: React.MouseEvent) => {
    if (e.target === e.currentTarget) {
      onClose();
    }
  };

  return (
    <div className="modal-overlay" onClick={handleBackdropClick}>
      <div className="modal-content education-modal">
        <div className="modal-header">
          <h2>{education.degree}</h2>
          <button className="modal-close" onClick={onClose}>
            <i className="fas fa-times"></i>
          </button>
        </div>
        
        <div className="modal-body">
          <div className="education-main-info">
            <div className="institution-info">
              <h3>
                <i className="fas fa-university"></i>
                {education.institution}
              </h3>
              {education.details?.college && education.details.college !== education.institution && (
                <p className="college-name">{education.details.college}</p>
              )}
              <div className="education-meta">
                <span className="duration">
                  <i className="fas fa-calendar"></i>
                  {education.duration}
                </span>
                <span className="location">
                  <i className="fas fa-map-marker-alt"></i>
                  {education.location}
                </span>
                {education.grade && (
                  <span className="grade">
                    <i className="fas fa-medal"></i>
                    {education.grade}
                  </span>
                )}
              </div>
            </div>
          </div>

          {education.description && (
            <div className="education-description">
              <p>{education.description}</p>
            </div>
          )}

          {education.details?.overview && (
            <div className="education-overview">
              <h4>Overview</h4>
              <p>{education.details.overview}</p>
            </div>
          )}

          {education.details?.academicPerformance && (
            <div className="academic-performance">
              <h4>Academic Performance</h4>
              <div className="performance-grid">
                <div className="performance-item">
                  <span className="label">Overall CGPA:</span>
                  <span className="value">{education.details.academicPerformance.overallCGPA}</span>
                </div>
                <div className="performance-item">
                  <span className="label">Classification:</span>
                  <span className="value">{education.details.academicPerformance.classification}</span>
                </div>
                {education.details.academicPerformance.peakSGPA && (
                  <div className="performance-item">
                    <span className="label">Peak SGPA:</span>
                    <span className="value">{education.details.academicPerformance.peakSGPA}</span>
                  </div>
                )}
              </div>
            </div>
          )}

          {education.details?.coreModules && education.details.coreModules.length > 0 && (
            <div className="core-modules">
              <h4>Core Modules</h4>
              <div className="modules-grid">
                {education.details.coreModules.map((module, index) => (
                  <div key={index} className="module-card">
                    <div className="module-header">
                      <h5>{module.name}</h5>
                      <div className="module-meta">
                        <span className="credits">{module.credits} credits</span>
                        <span className="grade">{module.grade}</span>
                      </div>
                    </div>
                    <p className="module-description">{module.description}</p>
                  </div>
                ))}
              </div>
            </div>
          )}

          {education.details?.coreSkills && education.details.coreSkills.length > 0 && (
            <div className="core-skills">
              <h4>Core Technical Skills</h4>
              <div className="skills-categories">
                {education.details.coreSkills.map((category, index) => (
                  <div key={index} className="skill-category">
                    <h5>{category.category}</h5>
                    <div className="skills-list">
                      {category.skills.map((skill, skillIndex) => (
                        <span key={skillIndex} className="skill-tag">{skill}</span>
                      ))}
                    </div>
                  </div>
                ))}
              </div>
            </div>
          )}

          {education.details?.technologies && education.details.technologies.length > 0 && (
            <div className="technologies">
              <h4>Technologies & Tools</h4>
              <div className="tech-tags">
                {education.details.technologies.map((tech, index) => (
                  <span key={index} className="tech-tag">{tech}</span>
                ))}
              </div>
            </div>
          )}

          {education.details?.laboratoryExperience && education.details.laboratoryExperience.length > 0 && (
            <div className="laboratory-experience">
              <h4>Laboratory Experience</h4>
              <div className="lab-list">
                {education.details.laboratoryExperience.map((lab, index) => (
                  <div key={index} className="lab-item">
                    <i className="fas fa-flask"></i>
                    <span>{lab}</span>
                  </div>
                ))}
              </div>
            </div>
          )}

          {education.details?.projectWork && education.details.projectWork.length > 0 && (
            <div className="project-work">
              <h4>Project Work</h4>
              <div className="project-list">
                {education.details.projectWork.map((project, index) => (
                  <div key={index} className="project-item">
                    <i className="fas fa-code"></i>
                    <span>{project}</span>
                  </div>
                ))}
              </div>
            </div>
          )}

          {education.details?.achievements && education.details.achievements.length > 0 && (
            <div className="education-achievements">
              <h4>Achievements</h4>
              <div className="achievements-list">
                {education.details.achievements.map((achievement, index) => (
                  <div key={index} className="achievement-item">
                    <i className="fas fa-trophy"></i>
                    <span>{achievement}</span>
                  </div>
                ))}
              </div>
            </div>
          )}
        </div>
      </div>
    </div>
  );
};

export default EducationModal;