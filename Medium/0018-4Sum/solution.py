# ═══════════════════════════════════════════════════════
#  Problem  : 0018. 4Sum
#  URL      : https://leetcode.com/problems/4sum/submissions/2070109090/
#  Difficulty : Medium
#  Language : Python
#  Runtime  : 425 ms
#  Memory   : 12.5 MB
#  Solved   : July 16, 2026
# ═══════════════════════════════════════════════════════

class Solution(object):
    def fourSum(self, nums, target):
        nums.sort()
        return self.kSum(nums, target, 4, 0)

    def kSum(self, nums, target, k, debut):
        resultats = []
        n = len(nums)

        # Pas assez d'éléments disponibles
        if n - debut < k:
            return resultats

        # Cas terminal : 2Sum
        if k == 2:
            gauche = debut
            droite = n - 1

            while gauche < droite:
                somme = nums[gauche] + nums[droite]

                if somme == target:
                    resultats.append([nums[gauche], nums[droite]])

                    gauche += 1
                    droite -= 1

                    while gauche < droite and nums[gauche] == nums[gauche - 1]:
                        gauche += 1

                    while gauche < droite and nums[droite] == nums[droite + 1]:
                        droite -= 1

                elif somme < target:
                    gauche += 1
                else:
                    droite -= 1

            return resultats

        # Réduction de k vers k - 1
        for i in range(debut, n - k + 1):
            if i > debut and nums[i] == nums[i - 1]:
                continue

            sous_resultats = self.kSum(
                nums,
                target - nums[i],
                k - 1,
                i + 1
            )

            for combinaison in sous_resultats:
                resultats.append([nums[i]] + combinaison)

        return resultats