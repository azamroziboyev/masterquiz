from docx import Document
import random
import os
import logging

logger = logging.getLogger(__name__)

def convert_format(doc, file_type="docx"):
    """
    Convert document format to quiz format
    Supports both Word (.docx) and text (.txt) files
    Returns a list of tuples: (question, [answers])
    where the first answer is always correct
    
    file_type: "docx" for Word documents, "txt" for text files
    """
    questions = []
    current_question = None
    options = []
    
    try:
        if file_type == "docx":
            # Parse Word document
            paragraph_texts = []
            for para in doc.paragraphs:
                text = para.text.strip()
                if text:  # Only add non-empty paragraphs
                    paragraph_texts.append(text)
            
            # First check for new format (starting with "?")
            new_format = False
            for text in paragraph_texts:
                if text.startswith("?"):
                    new_format = True
                    break
            
            if new_format:
                # Process using the new format (?Question, +Correct, -Wrong)
                for text in paragraph_texts:
                    # Check for the new format: ?savol
                    if text.startswith("?"):
                        # Save the previous question if exists
                        if current_question and options:
                            questions.append((current_question, options))
                            options = []
                        
                        current_question = text[1:].strip()  # Remove the '?' prefix
                        
                    # Answer format: +to'g'ri javob (correct) or -noto'g'ri javob (wrong)
                    elif text.startswith("+"):
                        correct_answer = text[1:].strip()
                        options.insert(0, correct_answer)  # Put correct answer first
                        
                    elif text.startswith("-"):
                        wrong_answer = text[1:].strip()
                        options.append(wrong_answer)
            else:
                # Process using the old format with ==== and +++++
                i = 0
                while i < len(paragraph_texts):
                    text = paragraph_texts[i]
                    
                    # Question separator
                    if text == "++++" or text.startswith("+++++"):
                        if current_question and options:
                            questions.append((current_question, options))
                            current_question = None
                            options = []
                            
                    # Options separator (skip)
                    elif text == "====" or text.startswith("====="):
                        pass
                        
                    # New question (if we don't have one yet and it doesn't start with #)
                    elif not current_question and not text.startswith('#'):
                        current_question = text
                        
                    # Correct answer
                    elif text.startswith('#'):
                        correct_answer = text[1:].strip()
                        options.insert(0, correct_answer)  # Put correct answer first
                        
                    # Wrong answer
                    elif text and current_question:
                        options.append(text.strip())
                        
                    i += 1
        
        elif file_type == "txt":
            # Parse text file content
            lines = []
            if isinstance(doc, str):
                lines = doc.strip().split('\n')
            else:
                lines = [line.strip() for line in doc]
                
            i = 0
            while i < len(lines):
                line = lines[i].strip()
                if not line:
                    i += 1
                    continue
                
                # New question format: ?savol
                if line.startswith("?"):
                    # Save previous question if exists
                    if current_question and options:
                        questions.append((current_question, options))
                        options = []
                    
                    current_question = line[1:].strip()  # Remove the '?' prefix
                
                # Answer format: +to'g'ri or -noto'g'ri
                elif line.startswith("+"):
                    correct_answer = line[1:].strip()
                    options.insert(0, correct_answer)  # Put correct answer first
                
                elif line.startswith("-"):
                    wrong_answer = line[1:].strip()
                    options.append(wrong_answer)
                
                # Original format support
                elif line == "++++" or line.startswith("+++++"):
                    if current_question and options:
                        questions.append((current_question, options))
                    current_question = None
                    options = []
                
                elif line == "====" or line.startswith("====="):
                    pass  # Skip delimiters
                
                elif not current_question and not line.startswith('#'):
                    current_question = line
                
                elif line.startswith('#'):
                    options.insert(0, line[1:].strip())  # Put correct answer first
                
                elif line and current_question:
                    options.append(line.strip())
                
                i += 1
                
        # Add the last question if we haven't done so already
        if current_question and options:
            questions.append((current_question, options))
    except Exception as e:
        logger.error(f"Error parsing document: {e}")
        
    return questions

def parse_text_file(file_content):
    """
    Parse text file content to extract questions and answers
    Supports the ?savol +to'g'ri -noto'g'ri format
    """
    return convert_format(file_content, file_type="txt")

def calculate_points(correct, total, system=100):
    """
    Calculate points based on scoring system
    system: 100 for 100-point system, 50 for 50-point system
    """
    if total == 0:
        return 0
    
    points = (correct / total) * system
    return round(points, 1)

def get_result_message(correct, total, lang="uz"):
    """
    Generate detailed test result message with improved formatting
    """
    if total == 0:
        return "Test natijasi yo'q" if lang == "uz" else "Нет результатов теста"
    
    wrong = total - correct
    percentage = (correct / total) * 100
    points_100 = calculate_points(correct, total, 100)
    points_50 = calculate_points(correct, total, 50)
    
    # Add emoji based on performance
    performance_emoji = "🎯"
    if percentage >= 90:
        performance_emoji = "🏆"
    elif percentage >= 70:
        performance_emoji = "🌟"
    elif percentage >= 50:
        performance_emoji = "👍"
    else:
        performance_emoji = "📚"
    
    # Create a progress bar
    bar_length = 10
    filled_length = int(round(bar_length * correct / total))
    progress_bar = "▓" * filled_length + "░" * (bar_length - filled_length)
    
    # Simplified results as requested
    if lang == "uz":
        result_message = f"""<b>{performance_emoji} TEST NATIJASI {performance_emoji}</b>

📊 <b>Foiz:</b> <code>{percentage:.1f}%</code>
{progress_bar}
💯 <b>Ball:</b> <code>{points_100}/100</code>
"""
    else:  # Russian
        result_message = f"""<b>{performance_emoji} РЕЗУЛЬТАТЫ ТЕСТА {performance_emoji}</b>

📊 <b>Процент:</b> <code>{percentage:.1f}%</code>
{progress_bar}
💯 <b>Баллы:</b> <code>{points_100}/100</code>
"""
    
    # Add a motivational message based on score
    if lang == "uz":
        if percentage >= 90:
            result_message += "\n🏆 <b>Ajoyib natija!</b> Tabriklaymiz!"
        elif percentage >= 70:
            result_message += "\n👏 <b>Yaxshi natija!</b> Davom eting!"
        elif percentage >= 50:
            result_message += "\n👍 <b>O'rtacha natija.</b> Ko'proq mashq qiling!"
        else:
            result_message += "\n📚 <b>Ko'proq o'qish va mashq qilish kerak!</b>"
    else:  # Russian
        if percentage >= 90:
            result_message += "\n🏆 <b>Отличный результат!</b> Поздравляем!"
        elif percentage >= 70:
            result_message += "\n👏 <b>Хороший результат!</b> Продолжайте!"
        elif percentage >= 50:
            result_message += "\n👍 <b>Средний результат.</b> Нужно больше практики!"
        else:
            result_message += "\n📚 <b>Нужно больше читать и практиковаться!</b>"
    
    return result_message
