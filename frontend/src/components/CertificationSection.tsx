import React from 'react';
import { Certification } from '../types/portfolio';
import './CertificationSection.css';

// Re-export for backward compatibility
export type { Certification } from '../types/portfolio';

interface CertificationSectionProps {
  certifications: Certification[];
}

const CertificationSection: React.FC<CertificationSectionProps> = ({ certifications }) => {
  return (
    <div className="section" id="certifications">
      <h2>Certifications</h2>
      <div className="certification-list">
        {certifications.map((cert) => (
          <div key={cert.id} className="certification-card">
            <h3>{cert.title || cert.name}</h3>
            <p>{cert.description}</p>
            <p><strong>Issued by:</strong> {cert.issuer}</p>
            <div className="certification-links">
              {cert.badgeUrl && (
                <a
                  href={cert.badgeUrl}
                  target="_blank"
                  rel="noopener noreferrer"
                  className="certification-link"
                >
                  <i className="fas fa-external-link-alt"></i> View Badge
                </a>
              )}
              {cert.certificateUrl && (
                <a
                  href={cert.certificateUrl}
                  target="_blank"
                  rel="noopener noreferrer"
                  className="certification-link"
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

export default CertificationSection;