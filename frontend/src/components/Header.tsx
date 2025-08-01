import React from 'react';
import './Header.css';

const Header: React.FC = () => {
  return (
    <div className="heading">
      <h1>
        <span className="hi">Hi, I'm </span>
        <span className="name">Mohammed Rishin Poolat </span>
        <span role="img" aria-label="Waving hand emoji">👋</span>
      </h1>
      <h3 className="designation">Software Engineer</h3>
      <div className="about">
        <p>
          Software Engineer with a Master's in Advanced Computer Science and Bachelor's in Computer Science and Engineering. Experienced in working across startup environments and established companies, with expertise in full-stack development using modern technologies like React, Next.js, Node.js, and TypeScript.
        </p>
        <p>
          Specialized in AI development including LLM integration, AI agents, and Model Context Protocol (MCP) implementation. Proven experience in building scalable web applications, e-commerce platforms, and automated systems. AWS Certified Cloud Practitioner with hands-on experience in cloud infrastructure and DevOps practices.
        </p>
        <p>
          Passionate about leveraging cutting-edge technologies to solve complex business problems and deliver impactful software solutions.
        </p>
      </div>
      <div className="links">
        <a
          href="https://www.linkedin.com/in/rishin-poolat/"
          target="_blank"
          rel="noopener noreferrer"
          title="LinkedIn"
          className="social-link"
        >
          <i className="fab fa-linkedin"></i>
        </a>
        <a
          href="https://github.com/rishinpoolat"
          target="_blank"
          rel="noopener noreferrer"
          title="GitHub"
          className="social-link"
        >
          <i className="fab fa-github"></i>
        </a>
        <a
          href="mailto:mohammedrishinpoolat@gmail.com"
          target="_blank"
          rel="noopener noreferrer"
          title="Email"
          className="social-link"
        >
          <i className="fas fa-envelope"></i>
        </a>
        <a
          href="/MohammedRishinPoolat.pdf"
          target="_blank"
          rel="noopener noreferrer"
        >
          <button className="resume-btn">Resume</button>
        </a>
      </div>
    </div>
  );
};

export default Header;