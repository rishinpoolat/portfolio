import React, { useState } from 'react';
import Header from './components/Header';
import Timeline from './components/Timeline';
import ExperienceSection from './components/ExperienceSection';
import EducationSection from './components/EducationSection';
import CertificationSection from './components/CertificationSection';
import HackathonSection from './components/HackathonSection';
import ProjectCard from './components/ProjectCard';
import ProjectModal from './components/ProjectModal';
import Footer from './components/Footer';
import { Project } from './types/portfolio';
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

  const handleProjectClick = (project: Project) => {
    setSelectedProject(project);
  };

  const handleCloseModal = () => {
    setSelectedProject(null);
  };

  return (
    <div className="container">
      <Header />
      
      <Timeline items={timelineData} />
      
      <ExperienceSection experiences={experienceData} />
      
      <EducationSection education={educationData} />
      
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
          onClose={handleCloseModal}
        />
      )}
      
      <Footer />
    </div>
  );
}

export default App;
