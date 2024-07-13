items = []

def get_all_items():
    return items

def get_item(item_id):
    return next((item for item in items if item['id'] == item_id), None)

def add_item(item):
    item['id'] = len(items)
    print(f"Adding item with ID: {item['id']}") 
    items.append(item)
    return item

def update_item(item_id, updated_item):
    print(f"Updating item with ID: {item_id}") 
    item = get_item(item_id)
    if item is not None:
        item.update(updated_item)
        return item
    return None

def delete_item(item_id):
    print(f"Deleting item with ID: {item_id}")
    item = get_item(item_id)
    if item is not None:
        items.remove(item)
        return item
    return None
