"""
Domain models for Job Organizer
"""
from dataclasses import dataclass
from typing import List, Optional
from enum import Enum


class JobStatus(str, Enum):
    """Job status enumeration"""
    WISHLIST = "WISHLIST"
    APPLIED = "APPLIED"
    INTERVIEW = "INTERVIEW"
    OFFER = "OFFER"
    REJECTED = "REJECTED"
    DISCARDED = "DISCARDED"
    ACTIVE = "ACTIVE"
    ALPHA = "ALPHA"
    PRIMARY = "PRIMARY"
    IDEA = "IDEA"
    POTENTIAL = "POTENTIAL"


class JobType(str, Enum):
    """Job type enumeration"""
    FULL_TIME = "FULL_TIME"
    PART_TIME = "PART_TIME"
    CONTRACT = "CONTRACT"
    INTERNSHIP = "INTERNSHIP"
    FREELANCE = "FREELANCE"
    OPEN_SOURCE = "OPEN_SOURCE"
    PROPOSAL = "PROPOSAL"


class Priority(str, Enum):
    """Priority enumeration"""
    HIGH = "HIGH"
    MEDIUM = "MEDIUM"
    LOW = "LOW"


@dataclass
class Job:
    """Job entity"""
    id: int
    title: str
    company: str
    location: str
    status: str
    priority: str
    type: str
    contact_website: Optional[str] = None
    description: Optional[str] = None
    score: int = 0
    technologies: List[str] = None
    requirements: List[str] = None
    benefits: List[str] = None
    responses: List[str] = None
    comments: Optional[str] = None
    situation: Optional[str] = None
    date_added: Optional[str] = None
    date_modified: Optional[str] = None
    
    def __post_init__(self):
        """Initialize default values for lists"""
        if self.technologies is None:
            self.technologies = []
        if self.requirements is None:
            self.requirements = []
        if self.benefits is None:
            self.benefits = []
        if self.responses is None:
            self.responses = []
    
    def to_dict(self) -> dict:
        """Convert to dictionary for Reflex state"""
        return {
            "id": self.id,
            "title": self.title,
            "company": self.company,
            "location": self.location,
            "status": self.status,
            "priority": self.priority,
            "type": self.type,
            "contact_website": self.contact_website,
            "description": self.description,
            "score": self.score,
            "technologies": self.technologies,
            "requirements": self.requirements,
            "benefits": self.benefits,
            "responses": self.responses,
            "comments": self.comments,
            "situation": self.situation,
            "date_added": self.date_added,
            "date_modified": self.date_modified,
        }
    
    @classmethod
    def from_dict(cls, data: dict) -> "Job":
        """Create Job from dictionary"""
        return cls(**data)


@dataclass
class Statistics:
    """Statistics entity"""
    total_jobs: int
    status_counts: dict
    priority_counts: dict
    
    @classmethod
    def from_dict(cls, data: dict) -> "Statistics":
        """Create Statistics from API response"""
        return cls(
            total_jobs=data.get("total_jobs", 0),
            status_counts=data.get("status_counts", {}),
            priority_counts=data.get("priority_counts", {}),
        )
