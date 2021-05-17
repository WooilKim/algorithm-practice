# https://leetcode.com/problems/minimum-difficulty-of-a-job-schedule/

from typing import List


class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        if len(jobDifficulty) < d:
            return -1
        elif len(jobDifficulty) == d:
            return sum(jobDifficulty)
        sorted_jobs = sorted(jobDifficulty, reverse=True)

        while len(jobDifficulty) > d:
            for job in sorted_jobs[1:]:
                idx = jobDifficulty.index(job)
                if (idx > 0 and jobDifficulty[idx - 1] >= job) or (
                        idx < len(sorted_jobs) - 1 and jobDifficulty[idx + 1] >= job):
                    sorted_jobs.remove(jobDifficulty[idx])
                    jobDifficulty = jobDifficulty[:idx] + jobDifficulty[idx + 1:]
                    break

        return sum(jobDifficulty)
    # print(days)


if __name__ == '__main__':
    # print(Solution().minDifficulty(jobDifficulty=[6, 5, 4, 3, 2, 1], d=2), 7)
    # print(Solution().minDifficulty(jobDifficulty=[9, 9, 9], d=4), -1)
    # print(Solution().minDifficulty(jobDifficulty=[11, 111, 22, 222, 33, 333, 44, 444], d=6), 843)
    print(Solution().minDifficulty([7, 1, 7, 1, 7, 1], 3), 15)
    print(Solution().minDifficulty([186, 398, 479, 206, 885, 423, 805, 112, 925, 656, 16, 932, 740, 292, 671, 360], 4),
          1803)
