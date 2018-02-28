#import de Textblob
from textblob import TextBlob
#import du classifieur Bayésien naïf
from textblob.classifiers import NaiveBayesClassifier

#import d'argparse afin de prendre en compte une phrase en argument
import argparse
parser = argparse.ArgumentParser(prog="class-pro-perso", description="Classifieur")
parser.add_argument("--phrase", type=str, help="Phrase à traiter", required=True)
args = parser.parse_args()
phrase_a_tester=args.phrase

#affichage de la phrase à classifier, passée en paramètre
print("Classification de la phrase : "+phrase_a_tester)

#ouverture du fichier d'entrainement
with open('exemples-entrainement.csv', 'r') as fp:
   #entraînement du classifieur
   cl = NaiveBayesClassifier(fp, format="csv")
   #nous soumettons la phrase au classifieur
   blob = TextBlob(phrase_a_tester, classifier=cl)
   prob_dist = cl.prob_classify(phrase_a_tester)
   #cette ligne nous affiche le label ayant la plus grande probabilité
   print("Cette phrase semble être de nature : "+prob_dist.max())

   #nous affichons ici la probabilité d'un label spécifique : pro
   print("Probabilité pro : "+str(round(prob_dist.prob("pro"), 2)))
   #nous affichons ici la probabilité d'un label spécifique : perso
   print("Probabilité perso : "+str(round(prob_dist.prob("perso"), 2)))