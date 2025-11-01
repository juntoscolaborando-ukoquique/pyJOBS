"""
API Client for Job Organizer
Handles all HTTP communication with the backend
"""
import httpx
import logging
from typing import List, Optional
from .config import config
from .models import Job, Statistics

logger = logging.getLogger(__name__)


class JobApiClient:
    """Client for interacting with the Job Organizer API"""
    
    def __init__(self):
        self.base_url = config.API_BASE_URL
        self.timeout = config.API_TIMEOUT
        logger.info(f"JobApiClient initialized with base_url={self.base_url}")
    
    async def fetch_statistics(self) -> Optional[Statistics]:
        """Fetch job statistics from the API"""
        logger.debug("Fetching statistics from API")
        try:
            async with httpx.AsyncClient() as client:
                response = await client.get(
                    f"{self.base_url}/stats",
                    timeout=self.timeout
                )
                
                if response.status_code == 200:
                    stats = Statistics.from_dict(response.json())
                    logger.info(f"Successfully fetched statistics: {stats.total_jobs} jobs")
                    return stats
                else:
                    logger.error(f"Failed to fetch stats: HTTP {response.status_code}")
                    return None
                    
        except httpx.ConnectError as e:
            logger.error(f"Connection error: Backend not reachable at {self.base_url}")
            return None
        except Exception as e:
            logger.exception(f"Unexpected error fetching statistics: {e}")
            return None
    
    async def fetch_jobs(
        self,
        status: Optional[str] = None,
        priority: Optional[str] = None
    ) -> List[Job]:
        """
        Fetch jobs from the API with optional filters
        
        Args:
            status: Filter by job status
            priority: Filter by priority
            
        Returns:
            List of Job objects
        """
        logger.debug(f"Fetching jobs with filters: status={status}, priority={priority}")
        try:
            # Build query parameters
            params = {}
            if status:
                params["status"] = status
            if priority:
                params["priority"] = priority
            
            async with httpx.AsyncClient() as client:
                response = await client.get(
                    f"{self.base_url}/jobs",
                    params=params,
                    timeout=self.timeout
                )
                
                if response.status_code == 200:
                    data = response.json()
                    jobs = [Job.from_dict(item) for item in data]
                    logger.info(f"Successfully fetched {len(jobs)} jobs")
                    return jobs
                else:
                    logger.error(f"Failed to fetch jobs: HTTP {response.status_code}")
                    return []
                    
        except httpx.ConnectError:
            logger.error(f"Connection error: Backend not reachable at {self.base_url}")
            return []
        except Exception as e:
            logger.exception(f"Unexpected error fetching jobs: {e}")
            return []
    
    async def health_check(self) -> bool:
        """Check if the API is reachable"""
        logger.debug("Performing health check")
        try:
            async with httpx.AsyncClient() as client:
                response = await client.get(
                    f"{self.base_url}/stats",
                    timeout=2.0
                )
                is_healthy = response.status_code == 200
                if is_healthy:
                    logger.info("Health check passed: API is reachable")
                else:
                    logger.warning(f"Health check failed: HTTP {response.status_code}")
                return is_healthy
        except Exception as e:
            logger.error(f"Health check failed: {e}")
            return False


# Create singleton instance
api_client = JobApiClient()
