import os
import unittest
from image_processing import *  

currentPath = os.path.abspath(__file__)

while os.path.basename(currentPath) != "Map":
    currentPath = os.path.dirname(currentPath)
    
os.chdir(currentPath)

awayFromBoss = set(os.path.join(currentPath + "/Images/Boss/Away from Boss", file) for file in os.listdir("Images/Boss/Away from Boss"))
nextToBoss = set(os.path.join(currentPath + "/Images/Boss/Next to Boss", file) for file in os.listdir("Images/Boss/Next to Boss"))

bossFiles = awayFromBoss.union(nextToBoss)

firstClueFiles = set(os.path.join(currentPath + "/Images/First Clue", file) for file in os.listdir("Images/First Clue"))
secondClueFiles = set(os.path.join(currentPath + "/Images/Second Clue", file) for file in os.listdir("Images/Second Clue"))
thirdClueFiles = set(os.path.join(currentPath + "/Images/Third Clue", file) for file in os.listdir("Images/Third Clue"))   

bossFiles = set(os.listdir("Images/Boss/Away from Boss") + os.listdir("Images/Boss/Next to Boss"))

firstClueFiles = set(os.listdir("Images/First Clue"))
secondClueFiles = set(os.listdir("Images/Second Clue"))
thirdClueFiles = set(os.listdir("Images/Third Clue"))


def getClue(fileName, clueNum):
    """
    Gets a clue from the appropraite folder based one the num.
    0 - > First Clue
    1 -> Second Clue
    2 -> Third Clue
    3 -> Boss
    """
    
    if clueNum == 0:
        return "Images/First Clue/" + fileName
    
    elif clueNum == 1:
        return "Images/Second Clue/" + fileName
    
    elif clueNum == 2:
        return "Images/Third Clue/" + fileName
    
    elif clueNum == 3:
        if os.path.exists("Images/Boss/Next to Boss/" + fileName):
            return "Images/Boss/Next to Boss/" + fileName
        elif os.path.exists("Images/Boss/Away from Boss/" + fileName):
            return "Images/Boss/Away from Boss/" + fileName
        
    return None
    


class BaseTests(unittest.TestCase):
    def test_1(self):
        self.assertEqual(1+1, 2)
        
    """def test_images_are_the_same(self):
        for file in firstClueFiles:
            filePath = getClue(file, 0)
            if file in secondClueFiles:
                score = compareImages(
                    getMap(filePath),
                    getMap(getClue(file, 1))
                )
                
                self.assertGreater(score, 0.6)
                
            if file in thirdClueFiles:
                score = compareImages(
                    getMap(filePath),
                    getMap(getClue(file, 2))
                )
                
                self.assertGreater(score, 0.6)
                
            if file in bossFiles:
                score = compareImages(
                    getMap(filePath),
                    getMap(getClue(file, 3))
                )
                
                self.assertGreater(score, 0.6)"""
                
    def test_get_Clue(self):
        self.assertEqual(getClue("13.jpg", 0), "Images/First Clue/13.jpg")
        self.assertEqual(getClue("13.jpg", 1), "Images/Second Clue/13.jpg")
        self.assertEqual(getClue("13.jpg", 2), "Images/Third Clue/13.jpg")
        self.assertEqual(getClue("11.jpg", 3), "Images/Boss/Away from Boss/11.jpg")
        self.assertEqual(getClue("13.jpg", 3), "Images/Boss/Next to Boss/13.jpg")
        
    def test_get_in_bounty(self):
        image = applyLevels(getMap(r"E:\replays\Hunt Showdown\Map\testing\images\Lawson 2C.jpg", True))
    
        self.assertEqual(getInBounty(image, LAWSON_POINTS, 20), {'GOLDEN': True, 'BLANC': True, 'GODARD': True, 'LAWSON': True, 'ARDEN': True, 'MAW': True})
        
        
        
        
        
        
        
        
        
        
        
        
        

from concurrent.futures import ThreadPoolExecutor

if __name__ == "__main__":
    test_classes = [BaseTests]

    with ThreadPoolExecutor() as executor:
        results = executor.map(lambda test_class: unittest.TextTestRunner().run(unittest.TestLoader().loadTestsFromTestCase(test_class)), test_classes)