# Render Deployment Guide - Job Organizer Reflex App

## 📋 Quick Start

Your Job Organizer is ready to deploy to Render! Follow these steps to get it live.

---

## ✅ Pre-Deployment Checklist

- ✅ **GitHub Repository:** https://github.com/juntoscolaborando-ukoquique/pyJOBS
- ✅ **Code Pushed:** All files committed and uploaded
- ✅ **render.yaml:** Configuration file ready
- ✅ **requirements.txt:** Dependencies listed
- ✅ **Render Account:** Created
- ✅ **Database:** job-organizer-db (dpg-d43t22re5dus73aakkt0-a)

---

## 🗄️ Database Credentials

**Database Name:** `job-organizer-db`  
**Database ID:** `dpg-d43t22re5dus73aakkt0-a`

**Internal Connection String:**
```
postgresql://job_organizer_user:YMNJsnKmOS6zDXziutmWbv5fDBw6h0Gy@dpg-d43t22re5dus73aakkt0-a/job_organizer
```

**Use this connection string for the `DATABASE_URL` environment variable in the backend service.**

---

## 🚀 Deployment Steps

### Step 1: Create Render Account

1. Go to https://render.com
2. Click **"Get Started"** or **"Sign Up"**
3. Sign up with:
   - GitHub (recommended - easier integration)
   - GitLab
   - Email

### Step 2: Connect GitHub Repository

1. **In Render Dashboard:**
   - Click **"New +"** button (top right)
   - Select **"Blueprint"**

2. **Connect GitHub:**
   - Click **"Connect GitHub"**
   - Authorize Render to access your repositories
   - Select **"juntoscolaborando-ukoquique"** organization
   - Grant access to **"pyJOBS"** repository

3. **Select Repository:**
   - Choose **"pyJOBS"** from the list
   - Render will detect `render.yaml` automatically

### Step 3: Configure Backend API URL

**IMPORTANT:** You need to update the API URL before deploying.

**Option A: Update render.yaml in GitHub**

1. Edit `render.yaml` in your repository
2. Update line 21:
   ```yaml
   - key: API_BASE_URL
     value: https://YOUR-BACKEND-URL.onrender.com/api
   ```
3. Commit and push:
   ```bash
   git add render.yaml
   git commit -m "Update API URL for Render deployment"
   git push origin main
   ```

**Option B: Set Environment Variable in Render**

1. After creating the service, go to **"Environment"** tab
2. Find `API_BASE_URL`
3. Update the value to your backend URL
4. Click **"Save Changes"**
5. Trigger manual deploy

### Step 4: Deploy with Blueprint

1. **Review Configuration:**
   - Service name: `job-organizer-reflex`
   - Environment: `Python`
   - Region: `Oregon` (or choose closest to you)
   - Plan: `Free` (or upgrade as needed)

2. **Click "Apply"**
   - Render will create the service
   - Build process will start automatically

3. **Monitor Build:**
   - Watch the build logs in real-time
   - Build takes ~5-10 minutes
   - Look for: "Build successful" message

### Step 5: Verify Deployment

1. **Get Your URL:**
   - Format: `https://job-organizer-reflex.onrender.com`
   - Click the URL in Render dashboard

2. **Test the App:**
   - ✅ Page loads with green theme
   - ✅ Click "🔄 Refresh Stats" - should load job counts
   - ✅ Click "📋 Load All Jobs" - should display jobs
   - ✅ Try filters - should filter jobs by status/priority

3. **Check Logs:**
   - Go to **"Logs"** tab in Render
   - Look for successful API connections
   - Check for any errors

---

## 🔧 Manual Deployment (Alternative)

If you prefer manual setup instead of Blueprint:

### Step 1: Create Web Service

1. Click **"New +"** → **"Web Service"**
2. Connect your GitHub repository
3. Select **"pyJobOrganizer"**

### Step 2: Configure Service

**Basic Settings:**
- **Name:** `job-organizer-reflex`
- **Region:** Oregon (or your preference)
- **Branch:** `main`
- **Runtime:** `Python 3`

**Build & Deploy:**
- **Build Command:**
  ```bash
  pip install --upgrade pip && pip install -r requirements.txt && reflex init
  ```
- **Start Command:**
  ```bash
  reflex run --env prod --backend-only
  ```

### Step 3: Environment Variables

Add these environment variables:

| Key | Value | Description |
|-----|-------|-------------|
| `PYTHON_VERSION` | `3.11.0` | Python version |
| `API_BASE_URL` | `https://your-backend.onrender.com/api` | Backend API URL |
| `ENVIRONMENT` | `production` | Environment name |
| `DEBUG` | `false` | Debug mode (off) |
| `PORT` | `8000` | Service port |

### Step 4: Advanced Settings

- **Health Check Path:** `/`
- **Auto-Deploy:** `Yes` (deploys on git push)

### Step 5: Create Service

Click **"Create Web Service"** and wait for deployment.

---

## 🔍 Backend API Requirements

Your Reflex app needs a FastAPI backend. Options:

### Option 1: Use Existing Local Backend

**Not recommended for production** - local backend not accessible from Render.

### Option 2: Deploy Backend to Render

1. Create another Render service for your FastAPI backend
2. Use that URL as `API_BASE_URL`
3. Example: `https://job-organizer-api.onrender.com/api`

### Option 3: Use External Backend

If your backend is hosted elsewhere:
- Ensure it's publicly accessible
- Use HTTPS (required for production)
- Update `API_BASE_URL` accordingly

---

## 📊 Expected Build Output

```
==> Downloading and installing Python 3.11.0
==> Installing dependencies from requirements.txt
Successfully installed reflex-0.8.17 ...
==> Running: reflex init
Initializing the web directory.
==> Build successful
==> Starting service with: reflex run --env prod --backend-only
Starting Reflex App
App running at: http://0.0.0.0:8000
```

---

## 🐛 Troubleshooting

### Warning: Invalid Node.js Version Detection

**Problem:** Reflex shows warning about invalid Node.js version during build
```
Warning: The detected version of /home/render/envwrappers/node (Invalid version: '::render::starttraceinternal::...')
```

**Cause:** Render's internal logging interferes with Node.js version detection

**Impact:** 
- ⚠️ Warning only - does not break the build
- Node.js 22.16.0 is still installed and used correctly
- Can be safely ignored

**Solution (Optional):**
To suppress this warning in future builds, you can:
1. Pin Node.js version in `package.json` (if you create one)
2. Or accept the warning - it doesn't affect functionality

**Status:** Non-critical - app works correctly despite warning

---

### Build Fails: "ModuleNotFoundError"

**Problem:** Missing dependencies

**Solution:**
```bash
# Check requirements.txt includes all packages
cat requirements.txt
# Should have: reflex, httpx, etc.
```

### Build Fails: "reflex init fails"

**Problem:** Reflex initialization error

**Solution:**
- Ensure build command includes `reflex init`
- Check Python version is 3.11+

### Runtime Error: "Cannot connect to API"

**Problem:** Backend API not accessible

**Solution:**
1. Check `API_BASE_URL` environment variable
2. Verify backend is running and accessible
3. Test backend URL in browser: `https://your-backend.onrender.com/api/stats`
4. Check backend CORS settings allow Render domain

### Service Spins Down (Free Tier)

**Problem:** Service sleeps after 15 minutes of inactivity

**Solution:**
- Use a service like UptimeRobot to ping your app every 10 minutes
- Upgrade to paid tier for always-on service
- Accept cold starts (first request takes ~30 seconds)

### Logs Show "Port already in use"

**Problem:** Port conflict

**Solution:**
- Render automatically assigns `PORT` environment variable
- Ensure your app uses `os.getenv("PORT", "8000")`
- Don't hardcode port numbers

---

## 🔐 Security Configuration

### CORS Settings (Backend)

Your FastAPI backend needs CORS configured:

```python
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "https://job-organizer-reflex.onrender.com",  # Your Render URL
        "http://localhost:3000",  # Local development
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
```

### Environment Variables

- Never commit `.env` files
- Use Render's environment variable UI
- Rotate secrets regularly

### HTTPS

- Render provides free SSL certificates
- Always use HTTPS in production
- Automatic certificate renewal

---

## 📈 Monitoring & Logs

### View Logs

1. Go to your service in Render dashboard
2. Click **"Logs"** tab
3. View real-time logs
4. Filter by log level (info, error, etc.)

### Health Checks

Render automatically monitors your service:
- Checks `/` endpoint every 30 seconds
- Restarts service if health check fails
- View health status in dashboard

### Metrics

Free tier includes:
- CPU usage
- Memory usage
- Request count
- Response times

---

## 🔄 Continuous Deployment

### Auto-Deploy on Git Push

Enabled by default:
```yaml
autoDeploy: true
```

**Workflow:**
1. Make code changes locally
2. Commit and push to GitHub:
   ```bash
   git add .
   git commit -m "Update feature"
   git push origin main
   ```
3. Render automatically detects push
4. Builds and deploys new version
5. Zero-downtime deployment

### Manual Deploy

1. Go to your service in Render
2. Click **"Manual Deploy"**
3. Select **"Deploy latest commit"**
4. Or choose specific commit from dropdown

### Rollback

1. Go to **"Events"** tab
2. Find previous successful deployment
3. Click **"Rollback to this version"**

---

## 💰 Pricing & Plans

### Free Tier

**Included:**
- 750 hours/month free
- Automatic SSL
- Continuous deployment
- Basic metrics

**Limitations:**
- Service spins down after 15 min inactivity
- Slower performance
- 512 MB RAM
- Shared CPU

### Starter Plan ($7/month)

- Always-on service
- 1 GB RAM
- Faster performance
- No spin-down

### Pro Plan ($25/month)

- 4 GB RAM
- Dedicated CPU
- Priority support
- Advanced metrics

---

## 🌐 Custom Domain (Optional)

### Add Custom Domain

1. Go to your service settings
2. Click **"Custom Domains"**
3. Click **"Add Custom Domain"**
4. Enter your domain: `jobs.yourdomain.com`

### Update DNS

Add CNAME record to your DNS:
```
Type: CNAME
Name: jobs
Value: job-organizer-reflex.onrender.com
```

### SSL Certificate

- Render automatically provisions SSL
- Takes ~5-10 minutes
- Automatic renewal

---

## ✅ Post-Deployment Checklist

- [ ] Service created in Render
- [ ] GitHub repository connected
- [ ] `API_BASE_URL` configured correctly
- [ ] Build completed successfully
- [ ] Service is running (green status)
- [ ] App accessible at Render URL
- [ ] Dashboard loads and displays stats
- [ ] Jobs list loads from backend
- [ ] Filters work correctly
- [ ] No errors in logs
- [ ] Health checks passing
- [ ] Auto-deploy enabled
- [ ] Custom domain configured (optional)

---

## 📞 Support Resources

### Render Documentation
- [Render Docs](https://render.com/docs)
- [Python on Render](https://render.com/docs/deploy-python)
- [Environment Variables](https://render.com/docs/environment-variables)
- [Custom Domains](https://render.com/docs/custom-domains)

### Reflex Documentation
- [Reflex Hosting](https://reflex.dev/docs/hosting/deploy/)
- [Reflex Environment Variables](https://reflex.dev/docs/api-reference/config/)

### Community
- [Render Community](https://community.render.com/)
- [Reflex Discord](https://discord.gg/reflex)

---

## 🎯 Quick Commands Reference

```bash
# Update and deploy changes
git add .
git commit -m "Your changes"
git push origin main

# View logs (if using Render CLI)
render logs -s job-organizer-reflex

# Trigger manual deploy (if using Render CLI)
render deploy -s job-organizer-reflex

# Check service status (if using Render CLI)
render services list
```

---

## 🎉 Success!

Your Job Organizer Reflex app is now deployed to Render!

**Your app URL:** `https://job-organizer-reflex.onrender.com`

**Next steps:**
1. Share the URL with users
2. Monitor logs for any issues
3. Set up custom domain (optional)
4. Consider upgrading to paid tier for better performance

---

**Created:** November 2, 2025  
**Repository:** https://github.com/juntoscolaborando-ukoquique/pyJOBS  
**Deployment Platform:** Render.com
