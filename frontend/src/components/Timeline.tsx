import React from 'react';
import './Timeline.css';

export interface TimelineItem {
  id: string;
  date: string;
  title: string;
  organization: string;
  location: string;
  type: 'education' | 'experience';
}

interface TimelineProps {
  items: TimelineItem[];
}

const Timeline: React.FC<TimelineProps> = ({ items }) => {
  return (
    <div className="section" id="timeline">
      <h2>Timeline</h2>
      <div className="timeline-container">
        {items.map((item, index) => (
          <div 
            key={item.id} 
            className="timeline-item"
            style={{ animationDelay: `${(index + 1) * 0.1}s` }}
          >
            <div className="timeline-date">{item.date}</div>
            <div className="timeline-content">
              <h3>{item.title}</h3>
              <p><strong>{item.organization}</strong></p>
              <p>{item.location}</p>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
};

export default Timeline;