def playlist(songs):
    hashmap = {}
    count = 0
    for i, song in enumerate(songs):
        remainder = song % 60
        diff = (60 - remainder) % 60 
        if diff in hashmap:
            hashmap[diff] += 1
            count += hashmap[diff]
        hashmap[diff] = 1
    return count

if __name__ == "__main__":
    songs = [10, 50, 90, 30]
    result = playlist(songs)
    print(f"Test case 1 --- Expected : 1, Output : {result}")

    # Test case 2
    songs = [30, 20, 150, 100, 40]
    result = playlist(songs)
    print(f"Test case 2 --- Expected : 3, Output : {result}")
    
    # Test Case 3
    songs = [60, 60, 60]
    result = playlist(songs)
    print(f"Test case 3 --- Expected : 3, Output : {result}")