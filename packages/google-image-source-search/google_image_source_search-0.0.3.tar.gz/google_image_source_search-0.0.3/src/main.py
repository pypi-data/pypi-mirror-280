from google_img_source_search import ReverseImageSearcher, SafeMode


if __name__ == '__main__':
    image_url = 'https://i.pinimg.com/originals/c4/50/35/c450352ac6ea8645ead206721673e8fb.png'
    # image_url = 'https://i.pinimg.com/oridginals/c4/50/35/c450352ac6ea8645ead206721673e8fb.png'



    rev_img_searcher = ReverseImageSearcher()
    rev_img_searcher.switch_safe_mode(SafeMode.DISABLED)
    res = rev_img_searcher.search(image_url)

    for search_item in res:
        print(f'Title: {search_item.page_title}')
        print(f'Site: {search_item.page_url}')
        print(f'Img: {search_item.image_url}\n')
