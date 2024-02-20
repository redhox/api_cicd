# Import des librairies
from unittest import TestCase, main
from fastapi.testclient import TestClient
from api import app


# assertEqual(a, b) : Vérifie si a est égal à b.
# assertNotEqual(a, b) : Vérifie si a est différent de b.
        
# assertIn(a, b) : Vérifie si a est dans b.
# assertNotIn(a, b) : Vérifie si a n'est pas dans b.
        
# assertIs(a, b) : Vérifie si a est b.
# assertIsNot(a, b) : Vérifie si a n'est pas b.
        
# assertTrue(x) : Vérifie si x est vrai.
# assertFalse(x) : Vérifie si x est faux.
        
# assertIsNone(x) : Vérifie si x est None.
# assertIsNotNone(x) : Vérifie si x n'est pas None.
        
# assertIsInstance(a, b) : Vérifie si a est une instance de b.
# assertNotIsInstance(a, b) : Vérifie si a n'est pas une instance de b.
        
# assertRaises(exc, fun, *args, **kwargs) : Vérifie si fun(*args, **kwargs) lève une exception de type exc.
# assertRaisesRegex(exc, r, fun, *args, **kwargs) : Vérifie si fun(*args, **kwargs) lève une exception de type exc et dont le message correspond à l'expression régulière r.


# Tests unitaire de l'environnement de développement
class TestDev(TestCase):

    # Vérifie que les fichiers sont présents
    def test_files(self):
        import os
        list_files = os.listdir()
        ...

    # Vérifie que le gitignore est présent
    

# Création du client de test

# Tests unitaire de l'API
    
    # Vérifie que l'API est bien lancée

    # Vérifie que l'API est bien lancée
    

    # Vérifie le endpoint hello_you
    

    # Vérifie le endpoint predict



# Test du modèle individuellement
#class TestModel(TestCase):
    

    # Vérifie que le modèle est bien chargé
    
    from unittest import TestCase, main
    from fastapi.testclient import TestClient
    from api import app  # Assurez-vous que le chemin d'importation est correct

    
    client = TestClient(app)  # Ajoutez cette ligne pour créer une instance de TestClient


    # Vérifie que les requirements sont présents
    def test_api_start(self):
        response = self.client.get("/hello")
        self.assertEqual(response.status_code,  200)
        self.assertEqual(response.json(), {"message": "Hello World"})
    def test_hello_you(self):
        response = self.client.get("/hello", params={"name": "John"})
        self.assertEqual(response.status_code,  200)
        self.assertEqual(response.json(), {"message": "Hello John"})
    # Votre méthode de test devrait maintenant fonctionner correctement
    def test_predict_endpoint(self):
        test_data = {
            "Gender":   1,
            "Age":   30,
            "Physical_Activity_Level":   2,
            "Heart_Rate":   80,
            "Daily_Steps":   10000,
            "BloodPressure_high":   120.0,
            "BloodPressure_low":   80.0
        }
        response = self.client.post("/predict", json=test_data)  # Utilisez self.client.post
        assert response.status_code ==   200
        # Vous pouvez ajouter d'autres assertions pour vérifier le contenu de la réponse
    def test_predict_endpoint2(self):
        test_data = {
            "Physical_Activity_Level":  30,
            "Heart_Rate":  70,
            "Daily_Steps":  7000,
        }
        response = self.client.post("/predict2", json=test_data)  # Utilisez self.client.post
        assert response.status_code ==   200
        
        
        
# Démarrage des tests
if __name__ == "__main__":
    main()

    

# Démarrage des tests
if __name__== "__main__" :
    main(
        verbosity=2,
    )
