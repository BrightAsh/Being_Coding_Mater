def solution(id_list, report, k):
    
    dic = {name:{'report_user': [], 'reported_user': []} for name in id_list}
    report = set(report)
    stopped_id = []
    answer = []
    
    for a in report:
        report_user,reported_user = a.split()
        dic[report_user]['report_user'].append(reported_user)
        dic[reported_user]['reported_user'].append(report_user)
    
    for user in id_list:
        if len(dic[user]['reported_user']) >= k:
            stopped_id.append(user)

    for user in id_list:
        answer.append(sum(reported_user in stopped_id for reported_user in dic[user]['report_user']))

    return answer