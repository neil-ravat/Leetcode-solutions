<!-- leetcode-notes-sync:start -->
# 1280. Students and Examinations

[Open on LeetCode](https://leetcode.com/problems/students-and-examinations/)

**Difficulty:** Easy

## My notes

### Submission notes

From accepted submission [#2192511258](https://leetcode.com/problems/students-and-examinations/submissions/2192511258/).

1280. Students and Examinations
Difficulty: Easy
Topic: CROSS JOIN, LEFT JOIN, GROUP BY, COUNT

Approach:
1. CROSS JOIN creates every student-subject pair.
2. LEFT JOIN matches examination records using BOTH
   student_id and subject_name.
3. Repeated examination records create multiple matches.
4. GROUP BY creates one group per student-subject pair.
5. COUNT(e.student_id) counts actual examinations,
   ignoring NULL values.
6. ORDER BY student_id, subject_name.

Important:
- COUNT(*) would incorrectly count unmatched pairs as 1.
- LEFT JOIN can increase row count when multiple matches exist.
- GROUP BY must include the subject to count separately.
- Always check the exact required sorting order.

Pattern:
Generate all combinations → Match records → Group → Count

## Accepted submissions

| Submission | Submitted (UTC) | Language | Code |
| --- | --- | --- | --- |
| [2192511258](https://leetcode.com/problems/students-and-examinations/submissions/2192511258/) | 2026-11-09 13:46:50 | mysql | [Source](submissions/2192511258.sql) |
| [2048007772](https://leetcode.com/problems/students-and-examinations/submissions/2048007772/) | 2026-06-27 15:58:05 | mysql | [Source](submissions/2048007772.sql) |
| [2047985637](https://leetcode.com/problems/students-and-examinations/submissions/2047985637/) | 2026-06-27 15:33:20 | mysql | [Source](submissions/2047985637.sql) |
<!-- leetcode-notes-sync:end -->
