# OncoTracker

**Technology Stack:** ASP.NET Core MVC, Entity Framework Core, SQLite, ASP.NET Core Identity, C#

## Overview

OncoTracker is a comprehensive cancer patient management web application built with ASP.NET Core MVC. The system facilitates seamless communication between cancer patients and their healthcare providers through appointment scheduling, medication tracking, and treatment progress monitoring.

## Key Features

### Patient Portal
- **Personal Dashboard**: View upcoming appointments, current medications, and treatment history
- **Appointment Booking**: Schedule appointments with assigned doctors for consultations, chemotherapy, scans, and other treatments
- **Medication Tracking**: Monitor prescribed medications and dosage schedules
- **Treatment History**: Access complete record of treatment updates and progress notes

### Doctor Portal
- **Patient Management**: Comprehensive patient list with detailed medical profiles
- **Appointment Management**: Approve/reject appointment requests and view schedules
- **Treatment Planning**: Add medications, schedule treatments, and update patient progress
- **Patient Assignment**: Assign new patients to your care

### Administrative Features
- **Role-based Authentication**: Secure login system with patient and doctor roles
- **Medical Records**: Cancer type, stage, diagnosis date tracking
- **Appointment Workflow**: Complete appointment lifecycle from request to completion
- **Data Security**: HIPAA-compliant patient data handling

## Technical Architecture

### Backend Framework
- **ASP.NET Core 9.0**: Modern web framework with MVC pattern
- **Entity Framework Core**: Object-relational mapping with SQLite database
- **ASP.NET Core Identity**: Authentication and authorization system

### Database Design
- **Patient Model**: Cancer type, stage, diagnosis date, assigned doctor
- **Doctor Model**: Specialization, license number, years of experience
- **Appointment Model**: Scheduling with status tracking (Pending, Approved, Completed, etc.)
- **Medication Model**: Prescription tracking with dosage and frequency
- **Treatment Updates**: Progress notes and medical history

### Security & Data Management
- **Identity Framework**: Secure user authentication with role management
- **Data Validation**: Comprehensive input validation and error handling
- **Database Migrations**: Version-controlled schema updates
- **GUID-based IDs**: Secure, non-sequential entity identification

## Key Controllers

- **PatientController**: Patient dashboard, appointments, medications, treatment history
- **DoctorController**: Doctor dashboard, patient management, appointment approval
- **AccountController**: User authentication and registration
- **AppointmentController**: Appointment CRUD operations and workflow management
- **MedicationController**: Prescription management and tracking

## Development Features

- **Responsive Design**: Mobile-friendly interface for both patients and doctors
- **Real-time Updates**: Dynamic appointment status changes and notifications
- **Data Seeding**: Automated initial data setup for development
- **Extensible Architecture**: Modular design for easy feature additions
- **Clean Code Practices**: SOLID principles and dependency injection

## Use Cases

- **Cancer Treatment Centers**: Streamline patient-doctor communication
- **Oncology Practices**: Centralized patient management system
- **Hospital Departments**: Integrated appointment and treatment tracking
- **Remote Care**: Enable telemedicine and remote patient monitoring

## Technical Highlights

- **Entity Relationships**: Complex many-to-many relationships between patients, doctors, and appointments
- **Business Logic**: Sophisticated appointment workflow and treatment tracking
- **User Experience**: Intuitive interfaces for both medical professionals and patients
- **Scalability**: Database design supports growing patient populations
- **Maintainability**: Clean architecture with separation of concerns

OncoTracker demonstrates proficiency in healthcare software development, complex database relationships, user authentication systems, and building real-world applications that solve genuine medical workflow challenges.