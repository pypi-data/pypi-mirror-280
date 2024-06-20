"""
    AC自动机，用于高效的关键词多模匹配
"""
import jieba

import re

from typing import Dict


class TrieNode:
    """
    Trie树的节点
    """

    def __init__(self):
        self.child = {}
        self.fail_to = None
        self.is_word = False
        #  下面节点值可以根据具体场景进行赋值
        self.str_ = ''


class AhoCorasickAutomation:
    """
    AC自动机，用于多模匹配，在使用前需要先根据词典创建Trie树，搜索时间性能O(N)

    Examples
    ----
    >>> wordlist = ["词语"]
    >>> ac_auto = AhoCorasickAutomation(wordlist)
    >>> ac_auto.search("包含词语的句子")
    {'词语': [(2, 3)]}
    """

    OUTPUT_ORIGINAL = 0  # 输出格式 {"关键词": [(开始位置, 结束位置), (开始位置, 结束位置)]}
    OUTPUT_LIST_ONLY_KEY = 1  # 输出格式 ["关键词", "关键词"]
    OUTPUT_STRING_WITH_SEMICOLON = 2  # 输出格式 "关键词;关键词"

    def __init__(self, words: list = None):
        self.root = TrieNode()
        if words:
            self.build_trie_tree(words)
            self.build_ac_from_trie()

    def build_trie_tree(self, words: list):
        """
        根据词典简历Trie树

        :param words: 需要多模匹配的词典
        """
        for word in words:
            cur = self.root
            for i, c in enumerate(word):
                if c not in cur.child:
                    cur.child[c] = TrieNode()
                ps = cur.str_
                cur = cur.child[c]
                cur.str_ = ps + c
            cur.is_word = True

    def build_ac_from_trie(self):
        """
        根据已经生成的Trie树构建AC自动机（失败指针等）
        """
        queue = []
        for child in self.root.child:
            self.root.child[child].fail_to = self.root
            queue.append(self.root.child[child])

        while len(queue) > 0:
            cur = queue.pop(0)
            for child in cur.child.keys():
                fail_to = cur.fail_to
                while True:
                    if fail_to is None:
                        cur.child[child].fail_to = self.root
                        break
                    if child in fail_to.child:
                        cur.child[child].fail_to = fail_to.child[child]
                        break
                    else:
                        fail_to = fail_to.fail_to
                queue.append(cur.child[child])

    def search(self, str_, post_process=True, use_jieba=True, output_mode=OUTPUT_ORIGINAL):
        """
        根据已经构建好的AC自动机对字符串进行多模匹配，时间性能O(len(str_))

        :param str_: 待搜索的字符串
        :param post_process: 若为True，则对AC自动机的搜索结果进行后处理，如处理匹配关键词重叠的情况
        :param use_jieba: 是否使用jieba分词
        :param output_mode: 仅当post_process为True有效；返回的结果格式，可选择AhoCorasickAutomation.OUTPUT_ORIGINAL等模式
        :return:
        """
        cur = self.root
        result = {}
        i_ = 0
        n = len(str_)
        while i_ < n:
            c = str_[i_]
            if c in cur.child:
                cur = cur.child[c]
                if cur.is_word:
                    temp = cur.str_
                    result.setdefault(temp, [])
                    result[temp].append([i_ - len(temp) + 1, i_])

                # 处理所有其他长度公共字串
                fl = cur.fail_to
                while fl:
                    if fl.is_word:
                        temp = fl.str_
                        result.setdefault(temp, [])
                        result[temp].append([i_ - len(temp) + 1, i_])
                    fl = fl.fail_to
                i_ += 1

            else:
                cur = cur.fail_to
                if cur is None:
                    cur = self.root
                    i_ += 1

        return self.post_process(result, output_mode=output_mode, use_jieba=use_jieba) if post_process else result

    @staticmethod
    def post_process(ac_result, output_mode=OUTPUT_ORIGINAL, use_jieba=False, seq_original=""):
        """
        用于后处理AC自动机扫描结果，处理多个关键词重叠情况，返回字符串
        :param ac_result: AC自动机的分词结果
        :param output_mode:  返回的结果格式，可选择AhoCorasickAutomation.OUTPUT_ORIGINAL等模式
        :param use_jieba: 是否使用jieba分词
        :param seq_original: AC分词结果的原字符串
        :return: 以';'连接的关键词，如“汽车;有限公司”
        """
        d_index = {}
        for key in ac_result:
            for index in ac_result[key]:
                d_index[(index[0], index[1])] = key

        d_index = sorted(d_index.items(), key=lambda x: x[0])

        # 结巴分词以区分交叉情况，如“佳保安全”
        if use_jieba and seq_original != "":
            list_cut = list(jieba.cut(seq_original))
            list_cut_position = []
            count_len = 0
            for i in range(len(list_cut)):
                list_cut_position.append(count_len)
                count_len = count_len + len(list_cut[i])
            to_delete = []
            for item in d_index:
                if [pos for pos in range(item[0][0] + 1, item[0][1] + 1) if pos in list_cut_position]:  # AC匹配到的结果包含切割点
                    if item[0][0] not in list_cut_position or item[0][1] + 1 not in list_cut_position:  # 起点与终点为切割点的排除
                        to_delete.append(item)
            d_index = [i for i in d_index if i not in to_delete]

        to_delete = []
        for i in range(len(d_index) - 1):
            if d_index[i][0][0] == d_index[i + 1][0][0]:  # 前缀相同，取长值
                to_delete.append(d_index[i])
        d_index = [i for i in d_index if i not in to_delete]

        i = 1
        while i < len(d_index):
            if d_index[i - 1][0][1] >= d_index[i][0][1]:  # 后缀小于前一个后缀，删除
                d_index.pop(i)
            else:
                i = i + 1

        list_result = [v for i, v in d_index]

        if output_mode == AhoCorasickAutomation.OUTPUT_ORIGINAL:
            result = {}
            for item in d_index:
                result[item[1]] = result.get(item[1], []) + [item[0]]
        elif output_mode == AhoCorasickAutomation.OUTPUT_LIST_ONLY_KEY:
            result = list_result
        elif output_mode == AhoCorasickAutomation.OUTPUT_STRING_WITH_SEMICOLON:
            result = ";".join(list_result)
        else:
            raise TypeError("指定的输出格式不合法")

        return result


class AhoCorasickAutomationConditionalFilter:
    """
        对AC自动机的结果根据条件进行过滤
        如输入文本 text = "非兼职"
        匹配的结果为{'兼职': [(1, 2)]}
        但由于词语"兼职"的附近 text[max(0, 1-3) min(len(text)-1, 2+3)]存在配置好的黑名单词"非"
        则会将"兼职"从匹配的结果中剔除
    """
    FILTER_MODE_BLACK = 0  # 若过滤器的模式为BLACK，则命中词与过滤词同时出现时，丢弃命中词
    FILTER_MODE_WHITE = 1  # 若过滤器的模式为WHITE，则除非命中词语过滤词同时出现保留，否则丢弃命中词

    def __init__(self, filter_map: Dict[str, list], distance=3, mode=FILTER_MODE_BLACK):
        """
            传入一个"命中词和需过滤词"组成的词典，初始化过滤器
        :param filter_map: 形如{"命中词": ["需过滤词1", "需过滤词2", ..]}
        """
        self.filter_map = filter_map
        self.filter_regex = {}
        for hit_word, black_words in filter_map.items():
            self.filter_regex[hit_word] = re.compile("|".join(black_words))
        self.distance = distance
        self.mode = mode

    def filter(self, text: str, original_ac_result: dict, distance=None):
        """
            传入的text应当尽量短，否则文本匹配将耗时
        :param text: 需过滤的原始文本，最好是分割后的短文本
        :param original_ac_result: AC自动机的原始返回结果，形如{'keyword': [(pos_start, pos_end), ..], ...}
        :param distance: 命中关键词前后搜索距离
        :return: 过滤后的hits
        """
        distance = distance or self.distance  # 若调用方法传入前后距离，则使用传入的参数，否则使用构造对象时的默认距离

        filtered_result = {}
        for hit, positions in original_ac_result.items():
            regex = self.filter_regex.get(hit)
            if not regex:  # 不需要过滤的命中词直接跳过
                filtered_result[hit] = positions
                continue

            legal_positions = []
            for pos in positions:
                text_hit_nearby = text[max(0, pos[0] - distance):min(len(text), pos[1] + distance + 1)]
                flag_hit_regex = len(re.findall(regex, text_hit_nearby)) > 0
                if (
                        (self.mode == self.FILTER_MODE_BLACK and flag_hit_regex) or
                        (self.mode == self.FILTER_MODE_WHITE and not flag_hit_regex)
                ):
                    continue
                legal_positions.append(pos)
            if legal_positions:
                filtered_result[hit] = legal_positions
        return filtered_result


if __name__ == '__main__':
    text_to_scan = "需要搜索的文本，其中可能包含关键词1，要求附近有条件1，关键词2由于不符合条件，所以将被过滤"

    # AC自动机多模匹配
    ac_auto_entity = AhoCorasickAutomation(["关键词1", "关键词2"])
    print(ac_auto_entity.search(text_to_scan))

    # 过滤器
    hits = ac_auto_entity.search(text_to_scan)
    ac_filter_entity = AhoCorasickAutomationConditionalFilter({
        "关键词1": ["条件1"],
        "关键词2": ["条件2"]
    }, distance=10, mode=AhoCorasickAutomationConditionalFilter.FILTER_MODE_WHITE)
    hits = ac_filter_entity.filter(text_to_scan, hits)
    print(hits)
