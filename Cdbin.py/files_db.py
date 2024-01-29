import re
from pymongo.errors import DuplicateKeyError
from pymongo import MongoClient
from info import DATABASE_URL, DATABASE_NAME, MAX_BTN

myclient = MongoClient(DATABASE_URL)
mydb = myclient[DATABASE_NAME]
mycol = mydb['Files']

async def save_file(media):
    """Save file in database"""

    file_name = re.sub(r"(_|\-|\.|\+)", " ", str(media.file_name))
    file = {
        '_id': media.file_unique_id,
        'file_name': file_name,
        'file_id': media.file_id,
        'file_size': media.file_size
    }
    try:
        mycol.insert_one(file)
        print(f'{file_name} is saved')
        return "Saved"
    except DuplicateKeyError:
        print(f'{file_name} is already saved')
        return "Duplicates"


async def get_database_size():
    size = mydb.command("dbstats")['dataSize']
    return size


async def total_files_count():
    count = mycol.count_documents({})
    return count


async def get_search_results(query, max_results=MAX_BTN, offset=0, filter=False, language=None):
    """For given query return (results, next_offset)"""

    query = query.strip()
    if filter:  # For better results
        query = query.replace(' ', r'(\s|\.|\+|\-|_)')
        raw_pattern = r'(\s|_|\-|\.|\+)' + query + r'(\s|_|\-|\.|\+)'
    if not query:
        raw_pattern = '.'
    elif ' ' not in query:
        raw_pattern = r'(\b|[\.\+\-_])' + query + r'(\b|[\.\+\-_])'
    else:
        raw_pattern = query.replace(' ', r'.*[\s\.\+\-_]')

    try:
        regex = re.compile(raw_pattern, flags=re.IGNORECASE)
    except:
        return None, None, None

    filter = {'file_name': regex}
    total_results = mycol.count_documents(filter)
    next_offset = offset + max_results
    if next_offset >= total_results:
        next_offset = ""
    cursor = mycol.find(filter)
    if language:
        lang_files = [file for file in cursor if language in file['file_name'].lower()]
        files = lang_files[offset:][:max_results]
        total_results = len(lang_files)
        next_offset = offset + max_results
        if next_offset >= total_results:
            next_offset = ""
        return files, next_offset, total_results
    cursor.skip(offset).limit(max_results)  # Slice files according to offset and max results
    files = list(cursor)
    return files, next_offset, total_results


async def get_file_details(file_unique_id):
    filter = {'_id': file_unique_id}
    file = mycol.find_one(filter)
    return file
