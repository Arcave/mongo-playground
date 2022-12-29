echo "URI: mongodb://localhost:27017"
echo "Username: root"
echo "Password: `kubectl get secret --namespace default mongo-mongodb -o jsonpath="{.data.mongodb-root-password}" | base64 -d`"