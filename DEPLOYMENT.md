# Deployment Guide - Job Organizer Reflex Edition

## 📦 GitHub Repository

- **URL:** https://github.com/juntoscolaborando-ukoquique/pyJOBS
- **Branch:** main

---

## 🚀 Deploying to Render

### Prerequisites
- ✅ **GitHub repository:** https://github.com/juntoscolaborando-ukoquique/pyJOBS
- ✅ **Code committed and pushed:** All files uploaded to GitHub
- ⏳ **Render account:** Sign up at https://render.com (free tier available)
- ⏳ **Backend API:** Your existing FastAPI backend URL

### Step 1: Prepare Backend API URL

You need your backend API URL for the Reflex app to connect to. This should be:
- Your existing FastAPI backend (currently at `http://localhost:8000/api`)
- If deploying backend to Render, it will be: `https://your-backend-name.onrender.com/api`

**Example:** `https://job-organizer-api.onrender.com/api`

### Step 2: Update render.yaml (Already Done)

The `render.yaml` file is ready but needs your backend API URL:
```yaml
envVars:
  - key: API_BASE_URL
    value: https://your-backend-api.onrender.com/api  # UPDATE THIS
```

### Step 3: Required Files (All Present)
- ✅ `requirements.txt` - Python dependencies
- ✅ `render.yaml` - Render configuration
- ✅ `.env.example` - Environment variables template
- ✅ Production-ready code structure

### Step 2: Configure Environment Variables

Update `render.yaml` with your backend API URL:
```yaml
envVars:
  - key: API_BASE_URL
    value: https://your-backend-api.onrender.com/api
```

### Step 3: Deploy to Render

#### Option A: Using Render Blueprint (Recommended)

1. Go to [Render Dashboard](https://dashboard.render.com/)
2. Click "New" → "Blueprint"
3. Connect your GitHub repository
4. Select the repository containing your Reflex app
5. Render will automatically detect `render.yaml`
6. Click "Apply" to deploy

#### Option B: Manual Deployment

1. Go to [Render Dashboard](https://dashboard.render.com/)
2. Click "New" → "Web Service"
3. Connect your GitHub repository
4. Configure:
   - **Name:** job-organizer-reflex
   - **Environment:** Python
   - **Build Command:** 
     ```bash
     pip install --upgrade pip && pip install -r requirements.txt && reflex init
     ```
   - **Start Command:**
     ```bash
     reflex run --env prod --backend-only
     ```
5. Add environment variables:
   - `API_BASE_URL`: Your backend API URL
   - `ENVIRONMENT`: production
   - `DEBUG`: false
   - `PORT`: 8000
6. Click "Create Web Service"

### Step 4: Verify Deployment

1. Wait for build to complete (~5-10 minutes)
2. Visit your Render URL: `https://your-app-name.onrender.com`
3. Test functionality:
   - Click "Refresh Stats"
   - Click "Load All Jobs"
   - Try filtering

### Step 5: Custom Domain (Optional)

1. In Render dashboard, go to your service
2. Click "Settings" → "Custom Domain"
3. Add your domain
4. Update DNS records as instructed

---

## 🔧 Configuration

### Environment Variables

| Variable | Description | Example |
|----------|-------------|---------|
| `API_BASE_URL` | Backend API endpoint | `https://api.example.com/api` |
| `API_TIMEOUT` | API request timeout (seconds) | `5.0` |
| `PORT` | Frontend port | `8000` |
| `ENVIRONMENT` | Environment name | `production` |
| `DEBUG` | Debug mode | `false` |

### Local Development

1. Copy environment template:
```bash
cp .env.example .env
```

2. Update `.env` with local values:
```env
API_BASE_URL=http://localhost:8000/api
ENVIRONMENT=development
DEBUG=True
```

3. Run locally:
```bash
./start.sh
```

---

## 📁 New Project Structure

```
job_organizer/
├── __init__.py
├── job_organizer.py      # Main app entry point (12 lines)
├── config.py             # Configuration with env vars
├── models.py             # Domain models (Job, Statistics)
├── api_client.py         # API communication layer
├── state.py              # Reflex state management
├── components.py         # Reusable UI components
└── pages.py              # Page layouts
```

### Benefits of New Structure

1. **Separation of Concerns**
   - Configuration isolated in `config.py`
   - API logic in `api_client.py`
   - UI components in `components.py`
   - State management in `state.py`

2. **Environment Support**
   - Easy to switch between dev/prod
   - Environment variables for sensitive data
   - No hardcoded URLs

3. **Testability**
   - Each module can be tested independently
   - Mock API client for testing
   - Isolated business logic

4. **Maintainability**
   - Smaller, focused files
   - Clear responsibilities
   - Easy to locate code

---

## 🔍 Troubleshooting

### Build Fails

**Error:** `ModuleNotFoundError: No module named 'reflex'`
**Solution:** Ensure `requirements.txt` includes `reflex==0.8.17`

**Error:** `reflex init` fails
**Solution:** Add `reflex init` to build command

### Runtime Errors

**Error:** Cannot connect to API
**Solution:** Check `API_BASE_URL` environment variable

**Error:** Port already in use
**Solution:** Render automatically assigns port via `PORT` env var

### Performance Issues

**Issue:** Slow initial load
**Solution:** 
- Render free tier may sleep after inactivity
- Consider paid tier for always-on service
- Use health checks to keep service warm

---

## 📊 Monitoring

### Health Checks

Render automatically monitors your service health.

Configure in `render.yaml`:
```yaml
healthCheckPath: /
```

### Logs

View logs in Render dashboard:
1. Go to your service
2. Click "Logs" tab
3. Monitor real-time logs

---

## 🔄 Continuous Deployment

### Auto-Deploy on Push

Render automatically deploys when you push to main branch.

To disable:
```yaml
autoDeploy: false
```

### Manual Deploy

1. Go to Render dashboard
2. Select your service
3. Click "Manual Deploy" → "Deploy latest commit"

---

## 💰 Cost Considerations

### Free Tier Limitations
- Service spins down after 15 minutes of inactivity
- 750 hours/month free
- Slower performance than paid tiers

### Paid Tier Benefits
- Always-on service
- Better performance
- More resources
- Custom domains included

---

## 🔐 Security Best Practices

1. **Never commit `.env` file**
   - Added to `.gitignore`
   - Use `.env.example` as template

2. **Use environment variables**
   - No hardcoded secrets
   - Configure in Render dashboard

3. **HTTPS only in production**
   - Render provides free SSL
   - Automatic certificate renewal

4. **API authentication**
   - Add API keys if needed
   - Use secure headers

---

## 📚 Additional Resources

- [Render Documentation](https://render.com/docs)
- [Reflex Deployment Guide](https://reflex.dev/docs/hosting/deploy/)
- [Environment Variables](https://render.com/docs/environment-variables)
- [Custom Domains](https://render.com/docs/custom-domains)

---

## ✅ Deployment Checklist

- [ ] Code refactored with new structure
- [ ] Environment variables configured
- [ ] `render.yaml` updated with backend URL
- [ ] Code pushed to GitHub
- [ ] Render service created
- [ ] Environment variables set in Render
- [ ] Build successful
- [ ] Service running
- [ ] API connection working
- [ ] Dashboard loads correctly
- [ ] Jobs list displays
- [ ] Filters working
- [ ] Custom domain configured (optional)

---

**Your Job Organizer is now production-ready for Render deployment! 🎉**
