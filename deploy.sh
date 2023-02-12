COMMIT_MSG="mod $(date +"%Y%m%d%I%M%S")"
git add .
git commit -m "$COMMIT_MSG"
git push
git push heroku main