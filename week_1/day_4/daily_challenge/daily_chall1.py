# ------ Exercise 1


class Pagination:
    def __init__(self, items=None, page_size=10):
        """
        Initialize a Pagination object.

        :param items: Optional list of items to paginate (default is empty list)
        :param page_size: Number of items per page (default is 10)
        """
        self.items = items if items is not None else []
        self.page_size = page_size

    def __repr__(self):
        return f"<Pagination total_items={len(self.items)} page_size={self.page_size}>"
    
    # ------ Exercise 2 

    import math

class Paginator:
    def __init__(self, items=None, page_size=10):
        # Initialize items as empty list if None
        if items is None:
            items = []
        self.items = items
        
        # Save page_size and initialize current index
        self.page_size = page_size
        self.current_idx = 0
        
        # Calculate total number of pages
        self.total_pages = math.ceil(len(self.items) / self.page_size)

# Example usage
p = Paginator([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], page_size=5)
print(p.total_pages)  # Output: 3
print(p.current_idx)  # Output: 0

# ------ Exercise 3

class Paginator:
    def __init__(self, items, page_size):
        self.items = items
        self.page_size = page_size
        self.current_idx = 0  # index of the first item on the current page

    def get_current_page_items(self):
        start = self.current_idx
        end = start + self.page_size
        return self.items[start:end]

    def next_page(self):
        if self.current_idx + self.page_size < len(self.items):
            self.current_idx += self.page_size

    def prev_page(self):
        if self.current_idx - self.page_size >= 0:
            self.current_idx -= self.page_size



# ------ Exercise 4 

class Paginator:
    def __init__(self, total_pages: int):
        if total_pages < 1:
            raise ValueError("There must be at least one page.")
        self.total_pages = total_pages
        self.current_index = 0  # internal 0-based index

    def go_to_page(self, page_num: int):
        """Go to the specified page number (1-based)."""
        if not 1 <= page_num <= self.total_pages:
            raise ValueError(f"Page number must be between 1 and {self.total_pages}")
        self.current_index = page_num - 1
        return self  # optional chaining if desired

    def first_page(self):
        """Navigate to the first page."""
        self.current_index = 0
        return self

    def last_page(self):
        """Navigate to the last page."""
        self.current_index = self.total_pages - 1
        return self

    def next_page(self):
        """Move one page forward, if not on the last page."""
        if self.current_index < self.total_pages - 1:
            self.current_index += 1
        return self

    def previous_page(self):
        """Move one page backward, if not on the first page."""
        if self.current_index > 0:
            self.current_index -= 1
        return self

    def current_page(self):
        """Return the current page number (1-based)."""
        return self.current_index + 1



# ------ Exercise 5 

class Pagination:
    def __init__(self, items, page_size):
        self.items = items
        self.page_size = page_size
        self.current_page = 0  # start at the first page

    def __str__(self):
        start = self.current_page * self.page_size
        end = start + self.page_size
        # Get items on the current page and join them with newline characters
        return "\n".join(str(item) for item in self.items[start:end])

# Example usage
alphabetList = list("abcdefghijklmnopqrstuvwxyz")
p = Pagination(alphabetList, 4)
print(str(p))


# ------ Exercise 6 

class Pagination:
    def __init__(self, items, page_size):
        if page_size <= 0:
            raise ValueError("page_size must be greater than 0")
        self.items = items
        self.page_size = page_size
        self.current_idx = 0  # page index, 0-based

    def get_visible_items(self):
        start = self.current_idx * self.page_size
        end = start + self.page_size
        return self.items[start:end]

    def next_page(self):
        if (self.current_idx + 1) * self.page_size < len(self.items):
            self.current_idx += 1

    def last_page(self):
        total_pages = (len(self.items) + self.page_size - 1) // self.page_size
        self.current_idx = total_pages - 1

    def go_to_page(self, page_number):
        if page_number <= 0:
            raise ValueError("Page number must be greater than 0")
        total_pages = (len(self.items) + self.page_size - 1) // self.page_size
        # Cap page_number to total_pages if it's too large
        self.current_idx = min(page_number - 1, total_pages - 1)
