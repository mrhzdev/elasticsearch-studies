curl -X GET \
  'http://localhost:9200/myindex/_analyze?pretty=true' \
  -H 'Content-Type: application/json' \
  -d '{
  "analyzer": "default",
  "text": "This is the default analyzer."
}'

MD will be improved