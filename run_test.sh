pytest --cov-report html --cov educatrice/tests
sonar-scanner \
  -Dsonar.projectKey=Garderie_Python \
  -Dsonar.sources=. \
  -Dsonar.host.url=http://localhost:9000/ \
  -Dsonar.token=sqp_4dafa58742da1b721cf641246c6aa80280619a70