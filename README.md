# gcp8ambatch

App Engine and CLOUD RUN commands:
----------------------------------

 gcloud run deploy backend-login-api   --source .   --region us-central1   --allow-unauthenticated   --platform managed
  313  curl -X POST https://backend-login-api-717948519217.us-central1.run.app/login   -H "Content-Type: application/json"   -d '{"username":"admin","password":"password123"}'
  314  cd ..
  315  mkdir -p lab-appengine-frontend
  316  cd lab-appengine-frontend
  317  vi main.py
  318  mkdir templates
  319  cd templates/
  320  vi login.html
  321  cd ..
  322  vi requirements.txt
  323  vi app.yml
  324  gcloud app deploy
  325  ls
  326  mv app.yml app.yaml
  327  ls
  328  gcloud app deploy
  329  ls
  330  cd lab-appengine-frontend/
  331  ls
  332  cat main.py 
  333  cd ..
  334  cd lab-cloudrun-backend/
  335  ls
  336  cat main.py 
  337  cat requirements.txt 
  338  cat Dockerfile 
  339  gcloud run deploy backend-login-api --source . --region us-central1 --allow-unauthenticated --platform managed
  340  cd ..
  341  cd lab-appengine-frontend/
  342  ls
  343  cat templates/login.html 
  344  ls
  345  cat main.py 
  346  cat app.yaml 
  347  vi app.yaml 
  348  cat app.yaml 
  349  gcloud app deploy
  350  vi app.yml
  351  vi app.yaml 
  352  gcloud app deploy
  353  cat main.py 
  354  clear
  355  cd ..
  356  cd lab-cloudrun-backend/
  357  cd ...
  358  cd ..
  359  cd lab-appengine-frontend/
  360  ls
  361  vi main.py 
  362  gcloud app deploy
  363  gcloud app logs tail -s default
  364  cat main.py 
  365  vi main.py 
  366  gcloud app deploy
  367  gcloud app logs tail -s default
  368  date
  369  gcloud app logs tail -s default
  370  cd lab-appengine-frontend/
  371  vi requirements.txt 
  372  vi main.py 
  373  gcloud app deploy
  374  gcloud app logs tail -s default
  375  vi main.py 
  376  gcloud app deploy
  377  vi main.py 
  378  vi app.yaml 
  379  gcloud app deploy
  380  gcloud run services get-iam-policy backend-login-api --region us-central1
  381  gcloud iam service-accounts list
  382  gcloud run services describe backend-login-api --region us-central1 --format="value(status.url)"
  383  vi main.py 
  384  cat app.yaml 
  385  gcloud run services describe backend-login-api --region us-central1 --format="value(status.url)"
  386  gcloud run services get-iam-policy backend-login-api --region us-central1
  387  cd ..
  388  cd lab-cloudrun-backend/
  389  ls
  390  gcloud run deploy backend-login-api --source . --region us-central1  --platform managed
  391  gcloud app logs tail -s default
  392  vi main.py 
  393  curl -X POST https://backend-login-api-717948519217.us-central1.run.app/login   -H "Content-Type: application/json"   -d '{"username":"admin","password":"password123"}'
  394  cd ..
  395  cd lab-appengine-frontend/
  396  vi main.py 
  397  vi app.yaml 
  398  gcloud app deploy
  399  gcloud run services remove-iam-policy-binding backend-login-api   --region us-central1   --member="serviceAccount:gcp-sa@project-125a5906-9774-4549-bad.iam.gserviceaccount.com"   --role="roles/run.invoker"
  400  gcloud run services add-iam-policy-binding backend-login-api   --region us-central1   --member="serviceAccount:gcp-sa@project-125a5906-9774-4549-bad.iam.gserviceaccount.com"   --role="roles/run.invoker"
  401  gcloud run services remove-iam-policy-binding backend-login-api   --region us-central1   --member="serviceAccount:gcp-sa@project-125a5906-9774-4549-bad.iam.gserviceaccount.com"   --role="roles/run.invoker"
  402  gcloud run services add-iam-policy-binding backend-login-api   --region us-central1   --member="serviceAccount:gcp-sa@project-125a5906-9774-4549-bad.iam.gserviceaccount.com"   --role="roles/run.invoker"
  403  gcloud run services get-iam-policy backend-login-api --region us-central1
  404  gcloud run services remove-iam-policy-binding backend-login-api   --region us-central1   --member="serviceAccount:gcp-sa@project-125a5906-9774-4549-bad.iam.gserviceaccount.com"   --role="roles/run.invoker"
  405  gcloud run services add-iam-policy-binding backend-login-api   --region us-central1   --member="serviceAccount:gcp-sa@project-125a5906-9774-4549-bad.iam.gserviceaccount.com"   --role="roles/run.invoker"
  406  cat main.py 
  407  ls
  408  cat main.py 
  409  cat requirements.txt 
  410  cat app.yaml 
  411  ls
  412  cd templates/
  413  ls
  414  cat login.html 
  415  ls
  416  cd ..
  417  ls
  418  cd lab-cloudrun-backend/
  419  ls
  420  cat main.py 
  421  ls
  422  cat requirements.txt 
  423  cat Dockerfile 
  424  ls
  425  cd ..
  426  ls
  427  mkdir lab-appengine-tasks-cron
  428  cd lab-appengine-tasks-cron/
  429  ls
  430  vi requirements.txt
  431  vi main.py
  432  vi cron.yaml
  433  vi app.yml
  434  vi app.yaml
  435  ls
  436  cd lab-appengine-
  437  cd lab-appengine-frontend/
  438  ls
  439  cat requirements.txt 
  440  cat main.py 
  441  gcloud run services get-iam-policy backend-login-api --region us-central1
  442  gcloud app deploy
  443  cat main.py 
  444  ls
  445  vi app.yaml 
  446  gcloud run services get-iam-policy backend-login-api --region us-central1
  447  cat app.yaml 
  448  gcloud app deploy
  449  vi app.yaml 
  450  gcloud app deploy
  451  gcloud run services get-iam-policy backend-login-api --region us-central1
  452  gcloud run services remove-iam-policy-binding backend-login-api --region us-central1 --member="serviceAccount:gcp-sa@project-125a5906-9774-4549-bad.iam.gserviceaccount.com" --role="role/run.invoker"
  453  gcloud app deploy
  454  vi app.yaml 
  455  gcloud app deploy
  456  gcloud config list
  457  gcloud run services get-iam-policy backend-login-api --region us-central1
  458  gcloud run services remove-iam-policy-binding backend-login-api --region us-central1 --member="serviceAccount:gcp-sa@project-125a5906-9774-4549-bad.iam.gserviceaccount.com" --role="roles/run.invoker"
  459  ls
  460  cd ..
  461  ls
  462  cd lab-appengine-tasks-cron/
  463  ls
  464  cat main.py 
  465  cat cron.yaml 
  466  ls
  467  cd ..
  468  cd lab-appengine-
  469  ls
  470  cd lab-appengine-frontend/
  471  ls
  472  cat templates/login.html 
  473  cd ..
  474  cd lab-appengine-tasks-cron/
  475  ls
  476  gcloud tasks queues create my-lab-queue --location=us-central1
  477  cat main.py 
  478  cat app.yaml 
  479  cat cron.yaml 
  480  gcloud app deploy
  481  gcloud app logs tail -s default
  482  curl https://project-125a5906-9774-4549-bad.uc.r.appspot.com/add-task
  483  gcloud app logs tail -s default
  484  cat main.py 
  485  cat cron.yaml 
  486  curl https://project-125a5906-9774-4549-bad.uc.r.appspot.com/add-task
  487  gcloud app logs tail -s default
  488  ls
  489  cd lab-appengine-tasks-cron/
  490  ls
  491  cat main.py 
  492  cat requirements.txt 
  493  cat app.yaml 
  494  ls
  495  ca t cron.yaml 
  496  cat cron.yaml 
  497  history