"""
Application State for Job Organizer
Manages all application state and business logic
"""
import reflex as rx
import logging
from typing import List, Dict, Any
from .api_client import api_client
from .models import Job, Statistics

logger = logging.getLogger(__name__)


class AppState(rx.State):
    """Application state with clean separation from API logic"""
    
    # Statistics
    total_jobs: int = 0
    status_counts: Dict[str, int] = {}
    priority_counts: Dict[str, int] = {}
    
    # Job list
    jobs: List[Dict[str, Any]] = []
    jobs_loaded: bool = False
    
    # Filters
    filter_status: str = ""
    filter_priority: str = ""
    
    # UI state
    api_status: str = "Not connected"
    api_error: str = ""
    
    async def fetch_stats(self):
        """Fetch statistics from API"""
        logger.info("Fetching statistics from backend")
        
        stats = await api_client.fetch_statistics()
        
        if stats:
            self.total_jobs = stats.total_jobs
            self.status_counts = stats.status_counts
            self.priority_counts = stats.priority_counts
            self.api_status = "Connected ✅"
            self.api_error = ""
            logger.info(f"Statistics updated: {self.total_jobs} jobs, {len(self.status_counts)} statuses")
        else:
            self.api_status = "Connection failed ❌"
            self.api_error = "Cannot connect to backend. Is it running?"
            logger.error("Failed to fetch statistics from backend")
    
    async def fetch_jobs(self):
        """Fetch jobs from API with current filters"""
        logger.info(f"Fetching jobs with filters: status={self.filter_status}, priority={self.filter_priority}")
        
        jobs = await api_client.fetch_jobs(
            status=self.filter_status if self.filter_status else None,
            priority=self.filter_priority if self.filter_priority else None
        )
        
        # Convert Job objects to dictionaries for Reflex state
        self.jobs = [job.to_dict() for job in jobs]
        self.jobs_loaded = True
        logger.info(f"Jobs loaded successfully: {len(self.jobs)} jobs")
    
    def set_status_filter(self, status: str):
        """Set status filter"""
        logger.debug(f"Setting status filter to: {status}")
        self.filter_status = status if status != "ALL" else ""
    
    def set_priority_filter(self, priority: str):
        """Set priority filter"""
        logger.debug(f"Setting priority filter to: {priority}")
        self.filter_priority = priority if priority != "ALL" else ""
    
    def clear_filters(self):
        """Clear all filters"""
        logger.info("Clearing all filters")
        self.filter_status = ""
        self.filter_priority = ""
