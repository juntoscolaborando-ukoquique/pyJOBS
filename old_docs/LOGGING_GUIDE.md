# Logging Guide - Job Organizer Reflex Edition

## Overview

The Job Organizer now uses Python's standard `logging` module for structured, professional logging instead of print statements. This provides better debugging, monitoring, and production support.

---

## 🎯 **Logging Configuration**

### Environment Variable

Control logging level via the `LOG_LEVEL` environment variable:

```bash
# .env file
LOG_LEVEL=INFO  # Options: DEBUG, INFO, WARNING, ERROR, CRITICAL
```

### Log Levels

| Level | When to Use | Example |
|-------|-------------|---------|
| **DEBUG** | Detailed diagnostic info | `logger.debug("Fetching jobs with filters: status=WISHLIST")` |
| **INFO** | General informational messages | `logger.info("Successfully fetched 29 jobs")` |
| **WARNING** | Warning messages | `logger.warning("Health check failed: HTTP 500")` |
| **ERROR** | Error messages | `logger.error("Connection error: Backend not reachable")` |
| **CRITICAL** | Critical errors | `logger.critical("Database connection lost")` |

---

## 📋 **Log Format**

All logs follow this format:
```
2025-11-01 04:20:00 - job_organizer.api_client - INFO - Successfully fetched 29 jobs
```

**Format breakdown:**
- `2025-11-01 04:20:00` - Timestamp
- `job_organizer.api_client` - Module name
- `INFO` - Log level
- `Successfully fetched 29 jobs` - Message

---

## 🔍 **Logging by Module**

### api_client.py

**Initialization:**
```python
logger.info("JobApiClient initialized with base_url=http://localhost:8000/api")
```

**API Calls:**
```python
logger.debug("Fetching statistics from API")
logger.info("Successfully fetched statistics: 29 jobs")
logger.error("Failed to fetch stats: HTTP 500")
```

**Errors:**
```python
logger.error("Connection error: Backend not reachable at http://localhost:8000/api")
logger.exception("Unexpected error fetching jobs: <exception details>")
```

### state.py

**State Operations:**
```python
logger.info("Fetching statistics from backend")
logger.info("Statistics updated: 29 jobs, 4 statuses")
logger.info("Fetching jobs with filters: status=WISHLIST, priority=HIGH")
logger.info("Jobs loaded successfully: 26 jobs")
```

**Filter Operations:**
```python
logger.debug("Setting status filter to: WISHLIST")
logger.info("Clearing all filters")
```

---

## 🚀 **Usage Examples**

### Development Mode (Verbose Logging)

```bash
# .env
LOG_LEVEL=DEBUG
ENVIRONMENT=development
```

**Output:**
```
2025-11-01 04:20:00 - job_organizer.api_client - INFO - JobApiClient initialized with base_url=http://localhost:8000/api
2025-11-01 04:20:01 - job_organizer.state - INFO - Fetching statistics from backend
2025-11-01 04:20:01 - job_organizer.api_client - DEBUG - Fetching statistics from API
2025-11-01 04:20:02 - job_organizer.api_client - INFO - Successfully fetched statistics: 29 jobs
2025-11-01 04:20:02 - job_organizer.state - INFO - Statistics updated: 29 jobs, 4 statuses
```

### Production Mode (Essential Logging Only)

```bash
# .env
LOG_LEVEL=WARNING
ENVIRONMENT=production
```

**Output:** Only warnings, errors, and critical messages

---

## 🐛 **Debugging with Logs**

### Enable Debug Logging

```bash
export LOG_LEVEL=DEBUG
./start.sh
```

### Common Debug Scenarios

**1. API Connection Issues:**
```
ERROR - Connection error: Backend not reachable at http://localhost:8000/api
```
**Solution:** Check if FastAPI backend is running on port 8000

**2. Empty Job List:**
```
INFO - Successfully fetched 0 jobs
```
**Solution:** Check filters or database content

**3. Filter Not Working:**
```
DEBUG - Setting status filter to: WISHLIST
INFO - Fetching jobs with filters: status=WISHLIST, priority=
DEBUG - Fetching jobs with filters: status=WISHLIST, priority=None
INFO - Successfully fetched 26 jobs
```
**Analysis:** Filter applied correctly, returned 26 WISHLIST jobs

---

## 📊 **Log Analysis**

### Successful Job Load Flow

```
INFO - Clearing all filters
INFO - Fetching jobs with filters: status=, priority=
DEBUG - Fetching jobs with filters: status=None, priority=None
INFO - Successfully fetched 29 jobs
INFO - Jobs loaded successfully: 29 jobs
```

### Failed API Connection Flow

```
INFO - Fetching statistics from backend
DEBUG - Fetching statistics from API
ERROR - Connection error: Backend not reachable at http://localhost:8000/api
ERROR - Failed to fetch statistics from backend
```

---

## 🔧 **Advanced Configuration**

### Custom Log File (Optional)

Modify `config.py` to add file logging:

```python
def setup_logging():
    """Configure application logging"""
    log_level = os.getenv("LOG_LEVEL", "INFO")
    log_format = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    
    handlers = [
        logging.StreamHandler(),  # Console output
        logging.FileHandler("job_organizer.log"),  # File output
    ]
    
    logging.basicConfig(
        level=getattr(logging, log_level.upper()),
        format=log_format,
        handlers=handlers
    )
```

### JSON Logging (Production)

For structured logging in production:

```python
import json
import logging

class JsonFormatter(logging.Formatter):
    def format(self, record):
        log_data = {
            "timestamp": self.formatTime(record),
            "level": record.levelname,
            "module": record.name,
            "message": record.getMessage(),
        }
        return json.dumps(log_data)
```

---

## 📈 **Monitoring in Production**

### Log Aggregation

Logs can be sent to monitoring services:
- **Datadog** - Application performance monitoring
- **Sentry** - Error tracking
- **CloudWatch** - AWS log aggregation
- **Render Logs** - Built-in on Render platform

### Key Metrics to Monitor

1. **Error Rate:** Count of ERROR/CRITICAL logs
2. **API Response Time:** Time between request and response logs
3. **Connection Failures:** Count of connection errors
4. **Job Load Success Rate:** Successful vs failed job fetches

---

## ✅ **Best Practices**

### DO ✅

```python
# Use appropriate log levels
logger.info("User action completed")
logger.error("Failed to connect to API")

# Include context in messages
logger.info(f"Successfully fetched {len(jobs)} jobs")
logger.error(f"Connection error: Backend not reachable at {self.base_url}")

# Use logger.exception for exceptions
except Exception as e:
    logger.exception(f"Unexpected error: {e}")
```

### DON'T ❌

```python
# Don't use print statements
print("Fetching jobs")  # ❌

# Don't log sensitive data
logger.info(f"API Key: {api_key}")  # ❌

# Don't use wrong log levels
logger.error("Starting application")  # ❌ (should be INFO)
```

---

## 🎯 **Benefits of Structured Logging**

1. **Debugging** - Trace application flow and identify issues
2. **Monitoring** - Track application health in production
3. **Auditing** - Record user actions and system events
4. **Performance** - Identify slow operations
5. **Troubleshooting** - Diagnose production issues remotely

---

## 📚 **Quick Reference**

### Change Log Level at Runtime

```bash
# Development
export LOG_LEVEL=DEBUG

# Production
export LOG_LEVEL=WARNING

# Restart application
./stop.sh && ./start.sh
```

### View Logs in Real-Time

```bash
# If using file logging
tail -f job_organizer.log

# On Render
# View logs in Render dashboard under "Logs" tab
```

---

## 🔗 **Related Documentation**

- [Python Logging Documentation](https://docs.python.org/3/library/logging.html)
- [Logging Best Practices](https://docs.python-guide.org/writing/logging/)
- [Render Logging](https://render.com/docs/logs)

---

**Your Job Organizer now has professional-grade logging for better debugging and monitoring! 📊**
