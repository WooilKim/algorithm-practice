# https://leetcode.com/problems/word-ladder-ii/
import math
from typing import List
from collections import deque, defaultdict


class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:

        wordSet = set(wordList)  # faster checks against dictionary
        if endWord not in wordSet:
            return []
        layer = {}
        layer[beginWord] = [[beginWord]]  # stores current word and all possible sequences how we got to it

        while layer:
            newlayer = defaultdict(list)  # returns [] on missing keys, just to simplify code
            for word in layer:
                if word == endWord:
                    return layer[word]  # return all found sequences
                for i in range(len(word)):  # change every possible letter and check if it's in dictionary
                    for c in 'abcdefghijklmnopqrstuvwxyz':
                        newWord = word[:i] + c + word[i + 1:]
                        if newWord in wordSet:
                            newlayer[newWord] += [j + [newWord] for j in layer[
                                word]]  # add new word to all sequences and form new layer element
            wordSet -= set(newlayer.keys())  # remove from dictionary to prevent loops
            layer = newlayer  # move down to new layer

        return []


class Solution2:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        min_len = math.inf
        answer = set()
        queue = deque()
        queue.append([beginWord])

        def get_adjacent(current, words):
            res = list()
            for word in words:
                if len(current) != len(word):
                    continue

                count = 0
                for c, w in zip(current, word):
                    if c != w:
                        count += 1

                if count == 1:
                    res.append(word)
            return res

        while queue:
            seq = queue.popleft()
            if len(seq) > min_len:
                continue
            if seq[-1] == endWord:
                answer.add(tuple(seq))
                min_len = len(seq)
                continue
            for word in get_adjacent(seq[-1], wordList):
                if word not in seq:
                    queue.append(seq + [word])
        answer = list(answer)
        answer.sort(key=lambda x: len(x))
        answer = [list(a) for a in answer if len(a) == len(answer[0])]
        return answer


if __name__ == '__main__':
    print(Solution().findLadders(beginWord="hit", endWord="cog", wordList=["hot", "dot", "dog", "lot", "log", "cog"]))
    print(Solution().findLadders("cet", "ism",
                                 [
                                     "kid", "tag", "pup", "ail", "tun", "woo", "erg", "luz", "brr", "gay", "sip", "kay",
                                     "per", "val", "mes", "ohs", "now", "boa", "cet", "pal", "bar", "die", "war", "hay",
                                     "eco", "pub", "lob", "rue", "fry", "lit", "rex", "jan", "cot", "bid", "ali", "pay",
                                     "col", "gum", "ger", "row", "won", "dan", "rum", "fad", "tut", "sag", "yip", "sui",
                                     "ark", "has", "zip", "fez", "own", "ump", "dis", "ads", "max", "jaw", "out", "btu",
                                     "ana", "gap", "cry", "led", "abe", "box", "ore", "pig", "fie", "toy", "fat", "cal",
                                     "lie", "noh", "sew", "ono", "tam", "flu", "mgm", "ply", "awe", "pry", "tit", "tie",
                                     "yet", "too", "tax", "jim", "san", "pan", "map", "ski", "ova", "wed", "non", "wac",
                                     "nut", "why", "bye", "lye", "oct", "old", "fin", "feb", "chi", "sap", "owl", "log",
                                     "tod", "dot", "bow", "fob", "for", "joe", "ivy", "fan", "age", "fax", "hip", "jib",
                                     "mel", "hus", "sob", "ifs", "tab", "ara", "dab", "jag", "jar", "arm", "lot", "tom",
                                     "sax", "tex", "yum", "pei", "wen", "wry", "ire", "irk", "far", "mew", "wit", "doe",
                                     "gas", "rte", "ian", "pot", "ask", "wag", "hag", "amy", "nag", "ron", "soy", "gin",
                                     "don", "tug", "fay", "vic", "boo", "nam", "ave", "buy", "sop", "but", "orb", "fen",
                                     "paw", "his", "sub", "bob", "yea", "oft", "inn", "rod", "yam", "pew", "web", "hod",
                                     "hun", "gyp", "wei", "wis", "rob", "gad", "pie", "mon", "dog", "bib", "rub", "ere",
                                     "dig", "era", "cat", "fox", "bee", "mod", "day", "apr", "vie", "nev", "jam", "pam",
                                     "new", "aye", "ani", "and", "ibm", "yap", "can", "pyx", "tar", "kin", "fog", "hum",
                                     "pip", "cup", "dye", "lyx", "jog", "nun", "par", "wan", "fey", "bus", "oak", "bad",
                                     "ats", "set", "qom", "vat", "eat", "pus", "rev", "axe", "ion", "six", "ila", "lao",
                                     "mom", "mas", "pro", "few", "opt", "poe", "art", "ash", "oar", "cap", "lop", "may",
                                     "shy", "rid", "bat", "sum", "rim", "fee", "bmw", "sky", "maj", "hue", "thy", "ava",
                                     "rap", "den", "fla", "auk", "cox", "ibo", "hey", "saw", "vim", "sec", "ltd", "you",
                                     "its", "tat", "dew", "eva", "tog", "ram", "let", "see", "zit", "maw", "nix", "ate",
                                     "gig", "rep", "owe", "ind", "hog", "eve", "sam", "zoo", "any", "dow", "cod", "bed",
                                     "vet", "ham", "sis", "hex", "via", "fir", "nod", "mao", "aug", "mum", "hoe", "bah",
                                     "hal", "keg", "hew", "zed", "tow", "gog", "ass", "dem", "who", "bet", "gos", "son",
                                     "ear", "spy", "kit", "boy", "due", "sen", "oaf", "mix", "hep", "fur", "ada", "bin",
                                     "nil", "mia", "ewe", "hit", "fix", "sad", "rib", "eye", "hop", "haw", "wax", "mid",
                                     "tad", "ken", "wad", "rye", "pap", "bog", "gut", "ito", "woe", "our", "ado", "sin",
                                     "mad", "ray", "hon", "roy", "dip", "hen", "iva", "lug", "asp", "hui", "yak", "bay",
                                     "poi", "yep", "bun", "try", "lad", "elm", "nat", "wyo", "gym", "dug", "toe", "dee",
                                     "wig", "sly", "rip", "geo", "cog", "pas", "zen", "odd", "nan", "lay", "pod", "fit",
                                     "hem", "joy", "bum", "rio", "yon", "dec", "leg", "put", "sue", "dim", "pet", "yaw",
                                     "nub", "bit", "bur", "sid", "sun", "oil", "red", "doc", "moe", "caw", "eel", "dix",
                                     "cub", "end", "gem", "off", "yew", "hug", "pop", "tub", "sgt", "lid", "pun", "ton",
                                     "sol", "din", "yup", "jab", "pea", "bug", "gag", "mil", "jig", "hub", "low", "did",
                                     "tin", "get", "gte", "sox", "lei", "mig", "fig", "lon", "use", "ban", "flo", "nov",
                                     "jut", "bag", "mir", "sty", "lap", "two", "ins", "con", "ant", "net", "tux", "ode",
                                     "stu", "mug", "cad", "nap", "gun", "fop", "tot", "sow", "sal", "sic", "ted", "wot",
                                     "del", "imp", "cob", "way", "ann", "tan", "mci", "job", "wet", "ism", "err", "him",
                                     "all", "pad", "hah", "hie", "aim", "ike", "jed", "ego", "mac", "baa", "min", "com",
                                     "ill", "was", "cab", "ago", "ina", "big", "ilk", "gal", "tap", "duh", "ola", "ran",
                                     "lab", "top", "gob", "hot", "ora", "tia", "kip", "han", "met", "hut", "she", "sac",
                                     "fed", "goo", "tee", "ell", "not", "act", "gil", "rut", "ala", "ape", "rig", "cid",
                                     "god", "duo", "lin", "aid", "gel", "awl", "lag", "elf", "liz", "ref", "aha", "fib",
                                     "oho", "tho", "her", "nor", "ace", "adz", "fun", "ned", "coo", "win", "tao", "coy",
                                     "van", "man", "pit", "guy", "foe", "hid", "mai", "sup", "jay", "hob", "mow", "jot",
                                     "are", "pol", "arc", "lax", "aft", "alb", "len", "air", "pug", "pox", "vow", "got",
                                     "meg", "zoe", "amp", "ale", "bud", "gee", "pin", "dun", "pat", "ten", "mob"]))
"""
bfs
queue
["hit"]
["hit" + @] if @ one diff not in 


"""
