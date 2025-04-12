import json
import os
import logging
from datetime import datetime
from typing import Dict, List, Tuple, Optional, Any

class TestStorage:
    """
    Class for storing and managing user tests
    """
    def __init__(self, storage_path: str = "user_tests.json"):
        self.storage_path = storage_path
        self.tests = self._load_tests()
    
    def _load_tests(self) -> Dict[str, List[Dict[str, Any]]]:
        """Load tests from file or create empty structure"""
        if os.path.exists(self.storage_path):
            try:
                with open(self.storage_path, 'r', encoding='utf-8') as f:
                    return json.load(f)
            except Exception as e:
                logging.error(f"Error loading tests: {e}")
        return {}
    
    def _save_tests(self) -> None:
        """Save tests to file"""
        try:
            with open(self.storage_path, 'w', encoding='utf-8') as f:
                json.dump(self.tests, f, ensure_ascii=False, indent=2)
        except Exception as e:
            logging.error(f"Error saving tests: {e}")
    
    def add_test(self, user_id: int, test_name: str, questions: List[Tuple[str, List[str]]]) -> None:
        """
        Add a new test for a user
        user_id: Telegram user ID
        test_name: Name of the test
        questions: List of (question, [answers]) tuples
        """
        user_id_str = str(user_id)
        
        if user_id_str not in self.tests:
            self.tests[user_id_str] = []
        
        # Convert questions to a serializable format
        serializable_questions = []
        for question, options in questions:
            serializable_questions.append({
                "question": question,
                "options": options
            })
        
        # Check if a test with this name already exists
        for test in self.tests[user_id_str]:
            if test["name"] == test_name:
                # Update existing test
                test["questions"] = serializable_questions
                test["updated_at"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                self._save_tests()
                return
        
        # Create new test
        self.tests[user_id_str].append({
            "name": test_name,
            "questions": serializable_questions,
            "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "updated_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        })
        
        self._save_tests()
    
    def get_user_tests(self, user_id: int) -> List[Dict[str, Any]]:
        """
        Get all tests for a user
        Each user only sees their own tests, even admins
        """
        user_id_str = str(user_id)
        return self.tests.get(user_id_str, [])
    
    def get_test(self, user_id: int, test_index: int) -> Optional[Dict[str, Any]]:
        """
        Get a specific test by index
        Returns formatted questions list [(question, [answers])]
        """
        user_id_str = str(user_id)
        if user_id_str not in self.tests or test_index >= len(self.tests[user_id_str]):
            return None
        
        test = self.tests[user_id_str][test_index]
        
        # Convert serialized questions to the format expected by the bot
        questions = []
        for q in test["questions"]:
            questions.append((q["question"], q["options"]))
        
        return {
            "name": test["name"],
            "questions": questions,
            "created_at": test["created_at"]
        }
    
    def delete_test(self, user_id: int, test_index: int) -> bool:
        """Delete a test by index"""
        user_id_str = str(user_id)
        if user_id_str not in self.tests or test_index >= len(self.tests[user_id_str]):
            return False
        
        self.tests[user_id_str].pop(test_index)
        self._save_tests()
        return True
