import React from 'react';
import { Education } from '../types/portfolio';
import './EducationSection.css';

// Re-export for backward compatibility
export type { Education } from '../types/portfolio';

interface EducationSectionProps {
  education: Education[];
  onEducationClick: (education: Education) => void;
}

const EducationSection: React.FC<EducationSectionProps> = ({ education, onEducationClick }) => {
  return (
    <div className="section" id="education">
      <h2>Education</h2>
      <div className="education-list">
        {education.map((edu) => (
          <div 
            key={edu.id} 
            className="education-card clickable"
            onClick={() => onEducationClick(edu)}
          >
            <div className="education-header">
              <h3>{edu.institution}</h3>
              {edu.grade && (
                <span className="grade-badge">{edu.grade}</span>
              )}
            </div>
            <p className="degree"><strong>{edu.degree}</strong></p>
            <div className="education-meta">
              <span className="duration">
                <i className="fas fa-calendar"></i>
                {edu.duration || `${edu.startDate} - ${edu.endDate}`}
              </span>
              <span className="location">
                <i className="fas fa-map-marker-alt"></i>
                {edu.location}
              </span>
            </div>
            {edu.description && (
              <p className="education-description">{edu.description}</p>
            )}
            <div className="click-hint">
              <i className="fas fa-eye"></i>
              Click to view details
            </div>
          </div>
        ))}
      </div>
    </div>
  );
};

export default EducationSection;