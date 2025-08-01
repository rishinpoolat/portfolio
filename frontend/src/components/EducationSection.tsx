import React from 'react';
import { Education } from '../types/portfolio';
import './EducationSection.css';

// Re-export for backward compatibility
export type { Education } from '../types/portfolio';

interface EducationSectionProps {
  education: Education[];
}

const EducationSection: React.FC<EducationSectionProps> = ({ education }) => {
  return (
    <div className="section" id="education">
      <h2>Education</h2>
      <div className="education-list">
        {education.map((edu) => (
          <div key={edu.id} className="education-card">
            <h3>{edu.institution}</h3>
            <p><strong>Course:</strong> {edu.degree}</p>
            <p><strong>Duration:</strong> {edu.duration || `${edu.startDate} - ${edu.endDate}`}</p>
            <p><strong>Location:</strong> {edu.location}</p>
          </div>
        ))}
      </div>
    </div>
  );
};

export default EducationSection;