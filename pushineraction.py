@sims4.commands.Command('pushinteraction', command_type=sims4.commands.CommandType.Live)
def pushinteraction(interaction:int,target:int,_connection=None):
    output = sims4.commands.CheatOutput(_connection)
    try:
        output("入力中...")
        agent = services.get_active_sim()
        output("シムのターゲット" + agent.full_name)
        manager = services.affordance_manager()
        client = services.client_manager().get(_connection)
        object_manager = services.object_manager()
        #候補追加
        for x in object_manager.values():
            if x.guid64 == target:
                candidacy.append(x)
        
        #最終候補選抜値
        
        #最終過程
        
        obj = candidacy[0]
        output(str(type(obj)))
        context = InteractionContext(agent, InteractionContext.SOURCE_PIE_MENU, Priority.High, client=client, pick=None)
        responce = agent.push_super_affordance(manager.get(interaction),obj,context)
        output(str(responce))
    except Exception as ex:
        pass
        output("エラー" + str(ex))
