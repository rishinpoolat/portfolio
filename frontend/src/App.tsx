import React, { useState } from 'react';
import Header from './components/Header';
import Timeline from './components/Timeline';
import ExperienceSection from './components/ExperienceSection';
import EducationSection from './components/EducationSection';
import EducationModal from './components/EducationModal';
import CertificationSection from './components/CertificationSection';
import HackathonSection from './components/HackathonSection';
import ProjectCard from './components/ProjectCard';
import ProjectModal from './components/ProjectModal';
import Footer from './components/Footer';
import { Project, Education } from './types/portfolio';
import {
  projects,
  timelineData,
  experienceData,
  educationData,
  certificationData,
  hackathonData
} from './data/portfolioData';
import './App.css';

function App() {
  const [selectedProject, setSelectedProject] = useState<Project | null>(null);
  const [selectedEducation, setSelectedEducation] = useState<Education | null>(null);

  const handleProjectClick = (project: Project) => {
    setSelectedProject(project);
  };

  const handleEducationClick = (education: Education) => {
    setSelectedEducation(education);
  };

  const handleCloseProjectModal = () => {
    setSelectedProject(null);
  };

  const handleCloseEducationModal = () => {
    setSelectedEducation(null);
  };

  return (
    <div className="container">
      <Header />
      
      <Timeline items={timelineData} />
      
      <ExperienceSection experiences={experienceData} />
      
      <EducationSection 
        education={educationData} 
        onEducationClick={handleEducationClick}
      />
      
      <CertificationSection certifications={certificationData} />
      
      <HackathonSection hackathons={hackathonData} />
      
      <div className="section" id="projects">
        <h2>Projects</h2>
        <div className="project-list">
          {projects.map((project) => (
            <ProjectCard
              key={project.id}
              project={project}
              onClick={() => handleProjectClick(project)}
            />
          ))}
        </div>
      </div>

      {selectedProject && (
        <ProjectModal
          project={selectedProject}
          onClose={handleCloseProjectModal}
        />
      )}

      {selectedEducation && (
        <EducationModal
          education={selectedEducation}
          onClose={handleCloseEducationModal}
        />
      )}
      
      <Footer />
    </div>
  );
}

export default App;
