# syp
Projet d'entrainement au python / Flask / HTML-CSS : Application d'aide au manager


Cette application doit permettre au manager de distribuer le travail à traiter aux différents collaborateurs qu'ils soit en présentiel ou en télétravail.
L'alimentation en nouveaux dossiers se fait par un fichier csv encodé en latin3 qui est exporté depuis une application métier (ILLIAD).

L'application se veut modulaire : d'autres suivit autres que les contentieux doivent pouvoir y être intégrés facilement.

L'application prévoit 2 typs d'utilisateurs : les managers et les collaborateurs.

Les managers doivent pouvoir : 
- créer les nouveau collaborateurs, mettre à jour leur données
- importer les nouvelles liste d'affaires
- affecter au agents disponibles les nouvelles affaires
- lancer le nettoyage des tables : enlever les affaire clôturées depuis longtemps,supprimer les agents qui ont quittés le service et effacés leur affaires cloturés
- cloturer les affaires après traitement dans applications métier


Les collaborateurs doivents pouvoir
- cloturer les affaires après traitement dans applications métier

L'application sera faite en python, htlm et css. Lorsqu'elle sera opérationnelle, du javascript sera utilisé
