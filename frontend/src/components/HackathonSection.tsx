import React from 'react';
import { Hackathon } from '../types/portfolio';
import './HackathonSection.css';

// Re-export for backward compatibility
export type { Hackathon } from '../types/portfolio';

interface HackathonSectionProps {
  hackathons: Hackathon[];
}

const HackathonSection: React.FC<HackathonSectionProps> = ({ hackathons }) => {
  return (
    <div className="section" id="hackathons">
      <h2>Hackathons</h2>
      <div className="hackathon-list">
        {hackathons.map((hackathon) => (
          <div key={hackathon.id} className="hackathon-card">
            <h3>{hackathon.title || hackathon.name}</h3>
            <p><strong>Project:</strong> {typeof hackathon.project === 'string' ? hackathon.project : hackathon.project?.name}</p>
            <p>{hackathon.description}</p>
            <p><strong>Issued by:</strong> {hackathon.issuer || hackathon.organizer}</p>
            <div className="hackathon-links">
              {hackathon.badgeUrl && (
                <a
                  href={hackathon.badgeUrl}
                  target="_blank"
                  rel="noopener noreferrer"
                  className="hackathon-link"
                >
                  <i className="fas fa-external-link-alt"></i> View Badge
                </a>
              )}
              {hackathon.certificateUrl && (
                <a
                  href={hackathon.certificateUrl}
                  target="_blank"
                  rel="noopener noreferrer"
                  className="hackathon-link"
                >
                  <i className="fas fa-external-link-alt"></i> View Certificate
                </a>
              )}
            </div>
          </div>
        ))}
      </div>
    </div>
  );
};

export default HackathonSection;