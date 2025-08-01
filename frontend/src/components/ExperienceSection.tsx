import React from 'react';
import { Experience } from '../types/portfolio';
import './ExperienceSection.css';

// Re-export for backward compatibility
export type { Experience } from '../types/portfolio';

interface ExperienceSectionProps {
  experiences: Experience[];
}

const ExperienceSection: React.FC<ExperienceSectionProps> = ({ experiences }) => {
  return (
    <div className="section" id="experience">
      <h2>Experience</h2>
      <div className="experience-list">
        {experiences.map((experience) => (
          <div key={experience.id} className="experience-card">
            <h3>{experience.title || experience.position}</h3>
            <p><strong>Company:</strong> {experience.company}</p>
            <p><strong>Duration:</strong> {experience.duration || `${experience.startDate} - ${experience.endDate}`}</p>
            <p><strong>Location:</strong> {experience.location}</p>
            <div className="responsibilities">
              {experience.responsibilities?.map((responsibility, index) => (
                <p key={index}>• {responsibility}</p>
              ))}
            </div>
          </div>
        ))}
      </div>
    </div>
  );
};

export default ExperienceSection;