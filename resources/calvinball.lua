_SETTINGS:SetPlayerMenuOff()
--_SETTINGS:SetPlayerMenuOn()
_SETTINGS:SetEraModern()
_SETTINGS:SetA2A_BRAA()
_SETTINGS:SetA2G_LL_DDM()

-- BASE:TraceOn()
-- BASE:TraceClass("CTLD_HERCULES")
-- BASE:TraceClass("CTLD")

MESSAGE:New("CALVINBALL BEGIN!", 5):ToAll()

local defaultDrive = lfs.writedir() .. string.format("Missions\\%s\\missionstate", MissionDb.missionName)

local function split(s, sep)
    local fields = {}
    local sep = sep or " "
    local pattern = string.format("([^%s]+)", sep)
    string.gsub(s, pattern, function(c) fields[#fields + 1] = c end)
    return fields
end

local function loadState()
    local states = {}
    local objectivevehiclegroupstates = {}
    local objectiveshipgroupstates = {}
    local objectivestaticgroupstates = {}
    local unitstates = {}
    local nodestates = {}
    local taskstates = {}
    local qrfstates = {}
    local reinformcementstates = {}
    local taskvehiclegroupstates = {}
    local taskshipgroupstates = {}
    local taskstaticgroupstates = {}
    local redairwingstates = {}
    local blueairwingstates = {}

    if io then
        if UTILS.CheckFileExists(defaultDrive,"progress.csv") then
            local _, loadeddata = UTILS.LoadFromFile(defaultDrive, "progress.csv")
            for _, _entry in pairs (loadeddata) do
                local dataset = UTILS.Split(_entry,",")
                -- name,state
                local name = dataset[1]
                local state = dataset[2]
                states[name] = state
            end
        end

        if UTILS.CheckFileExists(defaultDrive,"objectivevehiclegroups.csv") then
            local _, loadeddata = UTILS.LoadFromFile(defaultDrive, "objectivevehiclegroups.csv")
            for _, _entry in pairs (loadeddata) do
                local dataset = UTILS.Split(_entry,",")
                -- name,state
                local name = dataset[1]
                local state = dataset[2]
                objectivevehiclegroupstates[name] = state
            end
        end

        if UTILS.CheckFileExists(defaultDrive,"objectiveshipgroups.csv") then
            local _, loadeddata = UTILS.LoadFromFile(defaultDrive, "objectiveshipgroups.csv")
            for _, _entry in pairs (loadeddata) do
                local dataset = UTILS.Split(_entry,",")
                -- name,state
                local name = dataset[1]
                local state = dataset[2]
                objectiveshipgroupstates[name] = state
            end
        end

        if UTILS.CheckFileExists(defaultDrive,"objectivestaticgroups.csv") then
            local _, loadeddata = UTILS.LoadFromFile(defaultDrive, "objectivestaticgroups.csv")
            for _, _entry in pairs (loadeddata) do
                local dataset = UTILS.Split(_entry,",")
                -- name,state
                local name = dataset[1]
                local state = dataset[2]
                objectivestaticgroupstates[name] = state
            end
        end

        if UTILS.CheckFileExists(defaultDrive,"taskvehiclegroups.csv") then
            local _, loadeddata = UTILS.LoadFromFile(defaultDrive, "taskvehiclegroups.csv")
            for _, _entry in pairs (loadeddata) do
                local dataset = UTILS.Split(_entry,",")
                -- name,state
                local name = dataset[1]
                local state = dataset[2]
                taskvehiclegroupstates[name] = state
            end
        end

        if UTILS.CheckFileExists(defaultDrive,"taskshipgroups.csv") then
            local _, loadeddata = UTILS.LoadFromFile(defaultDrive, "taskshipgroups.csv")
            for _, _entry in pairs (loadeddata) do
                local dataset = UTILS.Split(_entry,",")
                -- name,state
                local name = dataset[1]
                local state = dataset[2]
                taskshipgroupstates[name] = state
            end
        end

        if UTILS.CheckFileExists(defaultDrive,"taskstaticgroups.csv") then
            local _, loadeddata = UTILS.LoadFromFile(defaultDrive, "taskstaticgroups.csv")
            for _, _entry in pairs (loadeddata) do
                local dataset = UTILS.Split(_entry,",")
                -- name,state
                local name = dataset[1]
                local state = dataset[2]
                taskstaticgroupstates[name] = state
            end
        end

        if UTILS.CheckFileExists(defaultDrive,"objectiveunits.csv") then
            local _, loadeddata = UTILS.LoadFromFile(defaultDrive, "objectiveunits.csv")
            for _, _entry in pairs (loadeddata) do
                local dataset = UTILS.Split(_entry,",")
                -- name,state
                local name = dataset[1]
                local state = dataset[2]
                unitstates[name] = state
            end
        end

        if UTILS.CheckFileExists(defaultDrive,"nodes.csv") then
            local _, loadeddata = UTILS.LoadFromFile(defaultDrive, "nodes.csv")
            for _, _entry in pairs (loadeddata) do
                local dataset = UTILS.Split(_entry,",")
                -- name,state
                local name = dataset[1]
                local state = dataset[2]
                nodestates[name] = state
            end
        end

        if UTILS.CheckFileExists(defaultDrive,"tasks.csv") then
            local _, loadeddata = UTILS.LoadFromFile(defaultDrive, "tasks.csv")
            for _, _entry in pairs (loadeddata) do
                local dataset = UTILS.Split(_entry,",")
                -- name,state
                local name = dataset[1]
                local state = dataset[2]
                taskstates[name] = state
            end
        end

        if UTILS.CheckFileExists(defaultDrive,"qrfs.csv") then
            local _, loadeddata = UTILS.LoadFromFile(defaultDrive, "qrfs.csv")
            for _, _entry in pairs (loadeddata) do
                local dataset = UTILS.Split(_entry,",")
                -- name,state
                local name = dataset[1]
                local state = dataset[2]
                qrfstates[name] = state
            end
        end

        if UTILS.CheckFileExists(defaultDrive,"reinforcements.csv") then
            local _, loadeddata = UTILS.LoadFromFile(defaultDrive, "reinforcements.csv")
            for _, _entry in pairs (loadeddata) do
                local dataset = UTILS.Split(_entry,",")
                -- name,state
                local name = dataset[1]
                local state = dataset[2]
                reinformcementstates[name] = state
            end
        end

        if UTILS.CheckFileExists(defaultDrive,"redairwings.csv") then
            local _, loadeddata = UTILS.LoadFromFile(defaultDrive, "redairwings.csv")
            for _, _entry in pairs (loadeddata) do
                local dataset = UTILS.Split(_entry,",")
                -- name,state
                local name = dataset[1]
                local state = dataset[2]
                redairwingstates[name] = state
            end
        end

        if UTILS.CheckFileExists(defaultDrive,"blueairwings.csv") then
            local _, loadeddata = UTILS.LoadFromFile(defaultDrive, "blueairwings.csv")
            for _, _entry in pairs (loadeddata) do
                local dataset = UTILS.Split(_entry,",")
                -- name,state
                local name = dataset[1]
                local state = dataset[2]
                blueairwingstates[name] = state
            end
        end
    end

    for _, objective in ipairs(MissionDb.objectives) do
        if states[objective.name] ~= nil then
            objective.state = states[objective.name]
        else
            objective.state = "unstarted"
        end
        for _, node in ipairs(objective.nodes) do
            if nodestates[node.name] ~= nil then
                node.state = nodestates[node.name]
            else
                node.state = "unstarted"
            end
        end
        for _, group in ipairs(objective.vehicleGroups) do
            if objectivevehiclegroupstates[group.name] ~= nil then
                group.state = objectivevehiclegroupstates[group.name]
            else
                group.state = "unactivated"
            end
        end
        for _, group in ipairs(objective.shipGroups) do
            if objectiveshipgroupstates[group.name] ~= nil then
                group.state = objectiveshipgroupstates[group.name]
            else
                group.state = "unactivated"
            end
        end
        for _, group in ipairs(objective.staticGroups) do
            if objectivestaticgroupstates[group.name] ~= nil then
                group.state = objectivestaticgroupstates[group.name]
            else
                group.state = "unactivated"
            end
        end
        for _, qrf in ipairs(objective.qrfs) do
            if qrfstates[qrf.name] ~= nil then
                qrf.state = qrfstates[qrf.name]
            else
                qrf.state = "unactivated"
            end
        end
        for _, reinforcement in ipairs(objective.reinforcements) do
            if reinformcementstates[reinforcement.name] ~= nil then
                reinforcement.state = reinformcementstates[reinforcement.name]
            else
                reinforcement.state = "unactivated"
            end
        end
        for _, task in ipairs(objective.tasks) do
            if taskstates[task.name] ~= nil then
                task.state = taskstates[task.name]
            else
                task.state = "unstarted"
            end
            for _, group in ipairs(task.vehicleGroups) do
                if taskvehiclegroupstates[group.name] ~= nil then
                    group.state = taskvehiclegroupstates[group.name]
                else
                    group.state = "unactivated"
                end
            end
            for _, group in ipairs(task.shipGroups) do
                if taskshipgroupstates[group.name] ~= nil then
                    group.state = taskshipgroupstates[group.name]
                else
                    group.state = "unactivated"
                end
            end
            for _, group in ipairs(task.staticGroups) do
                if taskstaticgroupstates[group.name] ~= nil then
                    group.state = taskstaticgroupstates[group.name]
                else
                    group.state = "unactivated"
                end
            end
        end
    end

    for name, state in pairs(unitstates) do
        MissionDb.units[name] = state
    end

    for _, airwing in ipairs(MissionDb.redchief.airwings) do
        if redairwingstates[airwing.name] ~= nil then
            airwing.state = redairwingstates[airwing.name]
        else
            airwing.state = "active"
        end
    end

    for _, airwing in ipairs(MissionDb.bluechief.airwings) do
        if blueairwingstates[airwing.name] ~= nil then
            airwing.state = blueairwingstates[airwing.name]
        else
            airwing.state = "active"
        end
    end

    -- todo, some sort of culling of the unit states from groups who are dead, since if they're dead we won't be spawning them again
end

local function saveState()
    if not lfs then
        return
    else
        lfs.mkdir(defaultDrive)
    end

    local objectivedata = ""
    local objectivevehiclegroupdata = ""
    local objectiveshipgroupdata = ""
    local objectivestaticgroupdata = ""
    local objectiveunitdata = ""
    local nodedata = ""
    local taskdata = ""
    local qrfdata = ""
    local reinforcementdata = ""
    local taskvehiclegroupdata = ""
    local taskshipgroupdata = ""
    local taskstaticgroupdata = ""
    local redairwingdata = ""
    local blueairwingdata = ""
    for _, objective in ipairs(MissionDb.objectives) do
        objectivedata = string.format("%s%s,%s\n",objectivedata, objective.name, objective.state)
        for _, group in ipairs(objective.vehicleGroups) do
            objectivevehiclegroupdata = string.format("%s%s,%s\n",objectivevehiclegroupdata, group.name, group.state)
        end
        for _, group in ipairs(objective.shipGroups) do
            objectiveshipgroupdata = string.format("%s%s,%s\n",objectiveshipgroupdata, group.name, group.state)
        end
        for _, group in ipairs(objective.staticGroups) do
            objectivestaticgroupdata = string.format("%s%s,%s\n",objectivestaticgroupdata, group.name, group.state)
        end
        for _, node in ipairs(objective.nodes) do
            nodedata = string.format("%s%s,%s\n",nodedata, node.name, node.state)
        end
        for _, task in ipairs(objective.tasks) do
            taskdata = string.format("%s%s,%s\n",taskdata, task.name, task.state)
            for _, group in ipairs(task.vehicleGroups) do
                taskvehiclegroupdata = string.format("%s%s,%s\n",taskvehiclegroupdata, group.name, group.state)
            end
            for _, group in ipairs(task.shipGroups) do
                taskshipgroupdata = string.format("%s%s,%s\n",taskshipgroupdata, group.name, group.state)
            end
            for _, group in ipairs(task.staticGroups) do
                taskstaticgroupdata = string.format("%s%s,%s\n",taskstaticgroupdata, group.name, group.state)
            end
        end
        for _, qrf in pairs(objective.qrfs) do
            qrfdata = string.format("%s%s,%s\n",qrfdata, qrf.name, qrf.state)
        end
        for _, reinforcement in pairs(objective.reinforcements) do
            reinforcementdata = string.format("%s%s,%s\n",reinforcementdata, reinforcement.name, reinforcement.state)
        end
    end
    for name, state in pairs(MissionDb.units) do
        objectiveunitdata = string.format("%s%s,%s\n",objectiveunitdata, name, state)
    end
    for _, airwing in pairs(MissionDb.redchief.airwings) do
        redairwingdata = string.format("%s%s,%s\n",redairwingdata, airwing.name, airwing.state)
    end
    for _, airwing in pairs(MissionDb.bluechief.airwings) do
        blueairwingdata = string.format("%s%s,%s\n",blueairwingdata, airwing.name, airwing.state)
    end

    UTILS.SaveToFile(defaultDrive,"progress.csv", objectivedata)
    UTILS.SaveToFile(defaultDrive,"objectivevehiclegroups.csv", objectivevehiclegroupdata)
    UTILS.SaveToFile(defaultDrive,"objectiveshipgroups.csv", objectiveshipgroupdata)
    UTILS.SaveToFile(defaultDrive,"objectivestaticgroups.csv", objectivestaticgroupdata)
    UTILS.SaveToFile(defaultDrive,"objectiveunits.csv", objectiveunitdata)
    UTILS.SaveToFile(defaultDrive,"nodes.csv", nodedata)
    UTILS.SaveToFile(defaultDrive,"tasks.csv", taskdata)
    UTILS.SaveToFile(defaultDrive,"qrfs.csv", qrfdata)
    UTILS.SaveToFile(defaultDrive,"reinforcements.csv", reinforcementdata)
    UTILS.SaveToFile(defaultDrive,"taskvehiclegroups.csv", taskvehiclegroupdata)
    UTILS.SaveToFile(defaultDrive,"taskshipgroups.csv", taskshipgroupdata)
    UTILS.SaveToFile(defaultDrive,"taskstaticgroups.csv", taskstaticgroupdata)
    UTILS.SaveToFile(defaultDrive,"redairwings.csv", redairwingdata)
    UTILS.SaveToFile(defaultDrive,"blueairwings.csv", blueairwingdata)
end

-- stupid forward declaration shit
local completeObjective

local function checkObjectiveCapture(objective)
    local isCaptured = true
    local tasksComplete = true
    for _, node in ipairs(objective.nodes) do
        node.opsZone:EvaluateZone()
        if node.opsZone:IsContested() then
            isCaptured = false
            break
        end
        if not (node.opsZone:IsGuarded() and node.opsZone:IsBlue()) then
            isCaptured = false
            break
        end
    end

    for _, task in ipairs(objective.tasks) do
        if not task.instance or not task.instance:IsDone() then
            tasksComplete = false
            break
        end
    end

    if isCaptured and tasksComplete then
        completeObjective(objective, objective.strand)
    end
end

local function buildStrandObjectiveStateMap()
    local strandObjectiveStateMap = {}
    for _, strand in ipairs(MissionDb.strands) do
        strandObjectiveStateMap[strand.name] = {
            unstarted = 0,
            active = 0,
            finished = 0,
            total = 0,
            activeObjective = {
                name = "",
                displayName = "",
                nodes = {},
                totalNodes = 0,
                capturedNodes = 0,
                tasks = {},
                totalTasks = 0,
                completedTasks = 0
            }
        }
        for _, objectiveName in ipairs(strand.sequence) do
            for _, objective in ipairs(MissionDb.objectives) do
                if objective.name == objectiveName then
                    strandObjectiveStateMap[strand.name].total = strandObjectiveStateMap[strand.name].total + 1
                    strandObjectiveStateMap[strand.name][objective.state] = strandObjectiveStateMap[strand.name][objective.state] + 1
                    if objective.state == "active" then
                        local objectiveZone = ZONE:FindByName(objective.name)
                        strandObjectiveStateMap[strand.name].activeObjective.displayName = objectiveZone:GetProperty("label")

                        for _, node in ipairs(objective.nodes) do
                            local nodeZone = ZONE:FindByName(node.name)
                            local nodeStatus = {
                                name  = nodeZone:GetProperty("label"),
                                captured = node.opsZone:IsGuarded() and node.opsZone:IsBlue(),
                                contested =  node.opsZone:IsContested(),
                                redUnitsCount = node.opsZone.Nred
                            }
                            strandObjectiveStateMap[strand.name].activeObjective.totalNodes = strandObjectiveStateMap[strand.name].activeObjective.totalNodes + 1
                            if nodeStatus.captured then
                                strandObjectiveStateMap[strand.name].activeObjective.capturedNodes = strandObjectiveStateMap[strand.name].activeObjective.capturedNodes + 1
                            end
                            table.insert(strandObjectiveStateMap[strand.name].activeObjective.nodes, nodeStatus)
                        end

                        for _, task in ipairs(objective.tasks) do
                            local taskZone = ZONE:FindByName(task.name)
                            local taskStatus = {
                                name = taskZone:GetProperty("label"),
                                complete = task.state == "finished",
                                auftrag = taskZone:GetProperty("auftrag")
                            }
                            strandObjectiveStateMap[strand.name].activeObjective.totalTasks = strandObjectiveStateMap[strand.name].activeObjective.totalTasks + 1
                            if taskStatus.complete then
                                strandObjectiveStateMap[strand.name].activeObjective.completedTasks = strandObjectiveStateMap[strand.name].activeObjective.completedTasks + 1
                            end
                            table.insert(strandObjectiveStateMap[strand.name].activeObjective.tasks, taskStatus)
                        end
                    end
                end
            end
        end
    end
    return strandObjectiveStateMap
end

local function showNodeCapturedUpdate(objective, node, captureOrLost)
    local objectiveZone = ZONE:FindByName(objective.name)
    local objectiveLabelText = objectiveZone:GetProperty("label")
    local nodeZone = ZONE:FindByName(node.name)
    local nodeLabelText = nodeZone:GetProperty("label")

    local strandObjectiveStateMap = buildStrandObjectiveStateMap()

    local strandName
    local props

    for sn, p in pairs(strandObjectiveStateMap) do
        if p.activeObjective.displayName == objectiveLabelText then
            strandName = sn
            props = p
            break
        end
    end

    local r = {}
    table.insert(r, "OBJECTIVE UPDATE")
    table.insert(r, "")
    table.insert(r, string.format("%s has been %s at objective %s", nodeLabelText, captureOrLost, objectiveLabelText))
    local m = table.concat(r, "\n")
    MESSAGE:New(m, 30):ToAll()
end

local function showObjectiveStartedUpdate(objective)
    local objectiveZone = ZONE:FindByName(objective.name)
    local objectiveLabelText = objectiveZone:GetProperty("label")

    local strandObjectiveStateMap = buildStrandObjectiveStateMap()

    local strandName
    local props

    for sn, p in pairs(strandObjectiveStateMap) do
        if p.activeObjective.displayName == objectiveLabelText then
            strandName = sn
            props = p
            break
        end
    end

    local r = {}
    table.insert(r, "OBJECTIVE UPDATE")
    table.insert(r, "")
    table.insert(r, string.format("Objective %s is now active in %s", objectiveLabelText, strandName))
    local m = table.concat(r, "\n")
    MESSAGE:New(m, 30):ToAll()
end

local function showObjectiveCompletedUpdate(completedObjective, strandName, casevacCount)
    local objectiveZone = ZONE:FindByName(completedObjective.name)
    local objectiveLabelText = objectiveZone:GetProperty("label")

    local r = {}
    table.insert(r, "OBJECTIVE UPDATE")
    table.insert(r, "")
    table.insert(r, string.format("Objective %s has been completed in %s", objectiveLabelText, strandName))
    table.insert(r, "")
    table.insert(r, "CASEVAC UPDATE")
    table.insert(r, "")
    table.insert(r, string.format("%i new CASEVAC requests in the objective area", casevacCount))
    local m = table.concat(r, "\n")
    MESSAGE:New(m, 30):ToAll()
end

local function showFarpUnlockedUpdate(farp, strandName)
    local zone = ZONE:FindByName(farp.name)
    local labelText = zone:GetProperty("label")

    local r = {}
    table.insert(r, "FARP UPDATE")
    table.insert(r, "")
    table.insert(r, string.format("%s is now unlocked in %s", labelText, strandName))
    local m = table.concat(r, "\n")
    MESSAGE:New(m, 30):ToAll()
end

local function showAirbaseUnlockedUpdate(airbase, strandName)
    local zone = ZONE:FindByName(airbase.name)
    local labelText = zone:GetProperty("label")

    local r = {}
    table.insert(r, "AIRBASE UPDATE")
    table.insert(r, "")
    table.insert(r, string.format("%s is now unlocked in %s", labelText, strandName))
    local m = table.concat(r, "\n")
    MESSAGE:New(m, 30):ToAll()
end


local function enemyReinforceZone(targetZoneName)
    local zone = ZONE:FindByName(targetZoneName)
    local label  = zone:GetProperty("label")
    local targetCoord = zone:GetCoordinate():GetClosestPointToRoad()

    local closestQrf = nil
    local closestQrfDistance = nil

    -- TODO: consider a max response distance, set as a property on the qrf zone
    for _, objective in ipairs(MissionDb.objectives) do
        for _, qrf in ipairs(objective.qrfs) do
            if qrf.state == "active" and #qrf.spawnGroups > 0 then
                local qrfZone = ZONE:FindByName(qrf.name)
                local qrfCoordinate = qrfZone:GetCoordinate()
                local distance = qrfCoordinate:DistanceFromPointVec2(targetCoord)
                if closestQrf == nil or distance < closestQrfDistance then
                    closestQrf = qrf
                    closestQrfDistance = distance
                end
            end
        end
    end

    if closestQrf ~= nil then
        local sg = closestQrf.spawnGroups[math.random(#closestQrf.spawnGroups)]
        local g = sg.instance:Spawn()

        g:OptionDisperseOnAttack(0)

        local ag = ARMYGROUP:New(g)
        ag:Activate()

        local gUnits = g:GetUnits()
        for _, gUnit in ipairs(gUnits) do
            if not gUnit:HasSEAD() then
                gUnit:OptionEngageRange(50)
            end
        end

        local guardMission = AUFTRAG:NewARMOREDGUARD(targetCoord)
        guardMission:SetEngageDetected()
        ag:AddMission(guardMission)

        function ag:OnAfterPassingWaypoint(From, Event, To, Waypoint)
            if ag:HasPassedFinalWaypoint() then
                MESSAGE:New(string.format("Enemy reinforcement convoy has arrived in %s.", label), 30):ToAll()
                guardMission:Cancel()
                local patrolMission = AUFTRAG:NewPATROLZONE(zone, ag:GetSpeedCruise())
                patrolMission:SetEngageDetected()
                ag:AddMission(patrolMission)

                -- Cancel the patrol mission after 5 minutes.
                SCHEDULER:New(nil, function()
                    patrolMission:Cancel()
                end, {}, 300)
            end
        end

        local sourceCoord =  ag:GetCoordinate()
        MESSAGE:New(string.format("Enemy reinforcement convoy enroute to %s from %s, traveling approximately %s km.", label, sourceCoord:ToStringMGRS(), UTILS.Round(closestQrfDistance/1000,0)), 30):ToAll()
    end

end

local function friendlyReinforceZone(targetZoneName)
    local zone = ZONE:FindByName(targetZoneName)
    local label  = zone:GetProperty("label")
    local targetCoord = zone:GetCoordinate():GetClosestPointToRoad()

    local closestReinforcement = nil
    local closestReinforcementDistance = nil

    -- TODO: consider a max response distance, set as a property on the reinforcement zone
    for _, objective in ipairs(MissionDb.objectives) do
        for _, reinforcement in ipairs(objective.reinforcements) do
            if reinforcement.state == "active" then
                local reinforcementZone = ZONE:FindByName(reinforcement.name)
                local reinforcementCoordinate = reinforcementZone:GetCoordinate()
                local distance = reinforcementCoordinate:DistanceFromPointVec2(targetCoord)
                if closestReinforcement == nil or distance < closestReinforcementDistance then
                    closestReinforcement = reinforcement
                    closestReinforcementDistance = distance
                end
            end
        end
    end

    if closestReinforcement ~= nil then
        local sg = closestReinforcement.spawnGroups[math.random(#closestReinforcement.spawnGroups)]
        local g = sg.instance:Spawn()

        g:OptionDisperseOnAttack(0)
        g:HandleEvent( EVENTS.Dead )
        function g:OnEventDead( EventData )
            -- 100% of the time...
            if math.random(1, 100) <= MissionDb.settings.blueCasevacChance then
                local c = EventData.IniGroup:GetCoordinate()
                if c then
                    MissionDb.csar.instance:SpawnCASEVAC(c:Translate(math.random(1, 10), math.random(0, 359)), coalition.side.BLUE, "CASEVAC", false, "CASEVAC", "CASEVAC", true)
                end
            end
        end

        local ag = ARMYGROUP:New(g)
        ag:Activate()

        local gUnits = g:GetUnits()
        for _, gUnit in ipairs(gUnits) do
            if not gUnit:HasSEAD() then
                gUnit:OptionEngageRange(50)
            end
        end

        local guardMission = AUFTRAG:NewARMOREDGUARD(targetCoord)
        guardMission:SetEngageDetected()
        ag:AddMission(guardMission)

        function ag:OnAfterPassingWaypoint(From, Event, To, Waypoint)
            if ag:HasPassedFinalWaypoint() then
                MESSAGE:New(string.format("Friendly reinforcement convoy has arrived in %s.", label), 30):ToAll()
                guardMission:Cancel()
                local patrolMission = AUFTRAG:NewPATROLZONE(zone, ag:GetSpeedCruise())
                patrolMission:SetEngageDetected()
                ag:AddMission(patrolMission)

                -- Cancel the patrol mission after 5 minutes.
                SCHEDULER:New(nil, function()
                    patrolMission:Cancel()
                end, {}, 300)
            end
        end

        local sourceCoord =  ag:GetCoordinate()
        MESSAGE:New(string.format("Friendly reinforcement convoy enroute to %s from %s, traveling approximately %s km.", label, sourceCoord:ToStringMGRS(), UTILS.Round(closestReinforcementDistance/1000,0)), 30):ToAll()
    end

end

local function randomEnemyReinforcement()
    local potentials = {}
    for _, objective in ipairs(MissionDb.objectives) do
        if objective.state == "active" then
            for _, node in ipairs(objective.nodes) do
                if node.state ~= "unstarted" then
                    table.insert(potentials, node.name)
                end
            end
        end
    end

    if #potentials > 0 then
        local chosenNodeName = potentials[math.random(#potentials)]
        enemyReinforceZone(chosenNodeName)
    end
end

local function randomFriendlyReinforcement()
    local potentials = {}
    for _, objective in ipairs(MissionDb.objectives) do
        if objective.state == "active" then
            for _, node in ipairs(objective.nodes) do
                if node.state ~= "unstarted" then
                    table.insert(potentials, node.name)
                end
            end
        end
    end

    if #potentials > 0 then
        local chosenNodeName = potentials[math.random(#potentials)]
        friendlyReinforceZone(chosenNodeName)
    end
end

local function standardAirwingReinforcement()
    local didIt = false
    for _, airwing in ipairs(MissionDb.redchief.airwings) do
        if airwing.state == "active" then
            for _, squadron in ipairs(airwing.squadrons) do
                local airwing = squadron.instance:GetAirwing()
                airwing:AddAssetToSquadron(squadron.instance, 1)
            end
            didIt = true
        end
    end
    if didIt then
        MESSAGE:New(string.format("New airframes have been delivered to the enemy warehouses"), 30):ToAll()
    end
end

local function nodeCaptured(objective, node, previousCoalition, newCoalition)
    if newCoalition == coalition.side.BLUE or previousCoalition == coalition.side.BLUE then
        if newCoalition == coalition.side.BLUE then
            showNodeCapturedUpdate(objective, node, "captured")
            if math.random(1, 100) <= 25 then
                enemyReinforceZone(node.name)
            end
        elseif previousCoalition == coalition.side.BLUE then
            showNodeCapturedUpdate(objective, node, "lost")
        end

        if math.random(1, 100) <= 50 then
            local nodeZone = ZONE:FindByName(node.name)
            local nodeLabel = nodeZone:GetProperty("label")
            MissionDb.csar.instance:SpawnCASEVAC(nodeZone:GetRandomPointVec2(), coalition.side.BLUE, string.format("%s casualty", nodeLabel), true, 'absolute unit', string.format("%s casualty", nodeLabel), true)
        end

        saveState()
    end

    checkObjectiveCapture(objective)
end

local function nodeGuarded(objective)
    checkObjectiveCapture(objective)
end

local function determineNextObjectiveFrom(objective)
    local strand
    for _, s in ipairs(MissionDb.strands) do
        if s.name == objective.strand then
            strand = s
            break
        end
    end

    local toStartName = nil

    for i, objectiveName in ipairs(strand.sequence) do
        if objectiveName == objective.name then
            local nextIndex = i+1
            if nextIndex <= #strand.sequence then
                toStartName = strand.sequence[i+1]
                break
            end
        end
    end

    if toStartName == nil then
        return nil
    end

    for _, objective in ipairs(MissionDb.objectives) do
        if objective.name == toStartName then
            return objective
        end
    end

    -- shouldn't get here
    return nil
end

local function spawnGroupsAtThing(thing, staticCountry)
    local skipGroupName = {}

    if thing.spawnGroups ~= nil then
        for _, group in ipairs(thing.spawnGroups) do
            skipGroupName[group.name] = true
        end
    end

    for _, category in ipairs({thing.vehicleGroups, thing.shipGroups}) do
        for _, group in ipairs(category) do
            if group.state ~= "dead" then
                if skipGroupName[group.name] ~= true then
                    group.state = "active"
                    local g = GROUP:FindByName(group.name)
                    if not g:IsActive() then
                        local gUnits = g:GetUnits()
                        for _, gUnit in ipairs(gUnits) do
                            if MissionDb.units[gUnit:Name()] == "dead" then
                                gUnit:Destroy(false)
                            else
                                MissionDb.units[gUnit:Name()] = "active"
                                if not gUnit:HasSEAD() then
                                    gUnit:OptionEngageRange(50)
                                end
                            end
                        end

                        g:OptionDisperseOnAttack(0)
                        g:Activate(0)

                        g:HandleEvent( EVENTS.Dead )
                        function g:OnEventDead( EventData )
                            MissionDb.units[EventData.IniUnitName] = "dead"
                            if g:CountAliveUnits() == 0 then
                                group.state = "dead"
                            end

                            if staticCountry == country.id.CJTF_BLUE then
                                -- 100% of the time...
                                if math.random(1, 100) <= MissionDb.settings.blueCasevacChance then
                                    local c = EventData.IniGroup:GetCoordinate()
                                    if c then
                                        MissionDb.csar.instance:SpawnCASEVAC(c:Translate(math.random(1, 10), math.random(0, 359)), coalition.side.BLUE, "CASEVAC", false, "CASEVAC", "CASEVAC", true)
                                    end
                                end
                            end
                        end
                    end
                end
            end
        end
    end

    if MissionDb.lateActivateStatics then
        for _, static in ipairs(thing.staticGroups) do
            if static.state ~= "dead" then
                static.state = "active"
                local ss = SPAWNSTATIC:NewFromTemplate(static.template, staticCountry)
                local s = ss:Spawn()
                -- For some reason, certain statics refuse to spawn.
                if s ~= nil then
                    s:HandleEvent( EVENTS.Dead )
                    function s:OnEventDead( EventData )
                        if EventData.IniUnitName == static.name then
                            static.state = "dead"
                        end
                    end
                end
            end
        end
    end

end

local function unlockFarpsForObjective(objective)
    for _, farp in ipairs(objective.farps) do
        spawnGroupsAtThing(farp, country.id.CJTF_BLUE)
        MissionDb.ctld.instance:AddCTLDZone(farp.name, CTLD.CargoZoneType.LOAD, SMOKECOLOR.Blue, true, false)

        local farpZone = ZONE:FindByName(farp.name)
        local farpLabelText = farpZone:GetProperty("label")
        farp.labelMarkId = farpZone:GetCoordinate(0):Translate(farpZone.Radius + 50, 0, false, true):TextToAll(farpLabelText, -1, {0,0,1}, 1, {1,1,1}, 0.0, 20, true)
        farp.circleMarkId = farpZone:GetCoordinate(0):CircleToAll(farpZone.Radius, -1, {0,0,1}, 1, {0,0,1}, 0.15, 2, true)

        for _, client in ipairs(farp.clients) do
            local farpSlot = USERFLAG:New(client)
            farpSlot:Set(0)
        end

        showFarpUnlockedUpdate(farp, objective.strand)

        SCHEDULER:New(nil, function()
            farpZone:GetCoordinate(0):SmokeGreen()
        end, {}, 1, 300)

        SCHEDULER:New(nil, function()
            farpZone:GetCoordinate(500):IlluminationBomb()
        end, {}, 1, 150)
    end
end

local function unlockAirbasesForObjective(objective)
    for _, airbase in ipairs(objective.airbases) do
        spawnGroupsAtThing(airbase, country.id.CJTF_BLUE)
        MissionDb.ctld.instance:AddCTLDZone(airbase.name, CTLD.CargoZoneType.LOAD, SMOKECOLOR.Blue, true, false)
        
        local airbaseZone = ZONE:FindByName(airbase.name)
        MissionDb.bluechief.instance:AddBorderZone(airbaseZone)

        for _, client in ipairs(airbase.clients) do
            local airbaseSlot = USERFLAG:New(client)
            airbaseSlot:Set(0)
        end

        showAirbaseUnlockedUpdate(airbase, objective.strand)
    end
end

local function unlockReinforcementsForObjective(objective)
    for _, reinforcement in ipairs(objective.reinforcements) do
        reinforcement.state = "active"
        spawnGroupsAtThing(reinforcement, country.id.CJTF_BLUE)
        for _, spawnGroup in ipairs(reinforcement.spawnGroups) do
            spawnGroup.instance = SPAWN:New(spawnGroup.name)
        end
    end
end

local function unlockQrfsForObjective(objective)
    for _, qrf in ipairs(objective.qrfs) do
        qrf.state = "active"
        spawnGroupsAtThing(qrf, country.id.CJTF_RED)
        for _, spawnGroup in ipairs(qrf.spawnGroups) do
            spawnGroup.instance = SPAWN:New(spawnGroup.name)
        end
    end
end

local function startObjective(objective)
    local objectiveZone = ZONE:FindByName(objective.name)

    if #objective.nodes > 0 then
        local objectiveLabelText = objectiveZone:GetProperty("label")
        objective.labelMarkId = objectiveZone:GetCoordinate(0):TextToAll(objectiveLabelText, -1, {0,0,0}, 1, {1,1,1}, 0.0, 20, true)

        MissionDb.redchief.conflictZones:AddZone(objectiveZone)
        MissionDb.bluechief.conflictZones:AddZone(objectiveZone)
    end

    for _, node in ipairs(objective.nodes) do
        local initialOwner = coalition.side.NEUTRAL
        if(node.state == "red") then
            initialOwner = coalition.side.RED
        elseif node.state == "blue" then
            initialOwner = coalition.side.BLUE
        end

        local nodeZone = ZONE:FindByName(node.name)
        node.opsZone = OPSZONE:New(nodeZone, initialOwner)
        node.opsZone:SetObjectCategories({Object.Category.UNIT})
        node.opsZone:SetDrawZone(true)
        node.opsZone:SetMarkZone(false)
        function node.opsZone:OnAfterCaptured(From, Event, To, Coalition)
            if Coalition == coalition.side.BLUE then
                node.state = "blue"
            elseif Coalition == coalition.side.RED then
                node.state = "red"
            end
            nodeCaptured(objective, node, node.opsZone:GetPreviousOwner(), Coalition)
        end
        function node.opsZone:OnAfterGuarded(From, Event, To)
            nodeGuarded(objective)
        end
        node.opsZone:Start()
        local nodeLabelText = nodeZone:GetProperty("label")
        node.labelMarkId = nodeZone:GetCoordinate(0):Translate(nodeZone.Radius + 50, 0, false, true):TextToAll(nodeLabelText, -1, {0,0,0}, 1, {1,1,1}, 0.0, 14, true)

        MissionDb.ctld.instance:AddCTLDZone(node.name, CTLD.CargoZoneType.MOVE, SMOKECOLOR.Blue, true, false)

        -- Temporarily disabled because it seems like they hyper-fixate on it instead of running missions in the general zone.
        --MissionDb.redchief.instance:AddStrategicZone(node.opsZone)
    end

    spawnGroupsAtThing(objective, country.id.CJTF_RED)

    for _, task in ipairs(objective.tasks) do
        if task.state ~= "finished" then
            spawnGroupsAtThing(task, country.id.CJTF_RED)

            local taskZone = ZONE:FindByName(task.name)
            local taskLabel = taskZone:GetProperty("label")
            local taskAuftrag = taskZone:GetProperty("auftrag")
            local taskDescription = taskZone:GetProperty("description")
            task.label = taskLabel

            -- Might consider FilterZones, but it only works for active units
            -- local targSet = SET_GROUP:New():FilterZones({taskZone}):FilterCoalitions("red"):FilterPrefixes(taskTargetNameContains):FilterOnce()
            if taskAuftrag == "ANTISHIP" then
                local taskGroupTargetNameContains = taskZone:GetProperty("groupTargetNameContains")
                local targSet = SET_GROUP:New():FilterCoalitions("red"):FilterPrefixes(taskGroupTargetNameContains):FilterOnce()
                local target = TARGET:New(targSet)
                task.instance = PLAYERTASK:New(AUFTRAG.Type.ANTISHIP, target, true , 99, "")
                task.instance:SetMenuName(taskLabel)
                task.instance:AddFreetext(taskDescription)

                local taskTargetUnitTypes = taskZone:GetProperty("targetUnitTypes")
                if taskTargetUnitTypes ~= "" then
                    task.instance:AddConditionSuccess(function()
                        local anyOfTypeAlive = true
                        targSet:ForEachGroup(function(g)
                            local gUnits = g:GetUnits()
                            for _, gUnit in ipairs(gUnits) do
                                if anyOfTypeAlive and gUnit:IsAlive() and string.match(taskTargetUnitTypes, gUnit:GetTypeName()) then
                                    anyOfTypeAlive = false
                                end
                            end
                        end)
                        return anyOfTypeAlive
                    end)
                end

                function task.instance:OnAfterSuccess(From, Event, To)
                    task.state = "finished"
                    checkObjectiveCapture(objective)
                    saveState()
                end

                MissionDb.strandtasks.instance:AddPlayerTaskToQueue(task.instance)
            elseif taskAuftrag == "SEAD" then
                local taskGroupTargetNameContains = taskZone:GetProperty("groupTargetNameContains")
                local targSet = SET_GROUP:New():FilterCoalitions("red"):FilterPrefixes(taskGroupTargetNameContains):FilterOnce()
                local target = TARGET:New(targSet)
                task.instance = PLAYERTASK:New(AUFTRAG.Type.SEAD, target, true , 99, "")
                task.instance:SetMenuName(taskLabel)
                task.instance:AddFreetext(taskDescription)

                local taskTargetUnitTypes = taskZone:GetProperty("targetUnitTypes")
                if taskTargetUnitTypes ~= "" then
                    task.instance:AddConditionSuccess(function()
                        local anyOfTypeAlive = true
                        targSet:ForEachGroup(function(g)
                            local gUnits = g:GetUnits()
                            for _, gUnit in ipairs(gUnits) do
                                if anyOfTypeAlive and gUnit:IsAlive() and string.match(taskTargetUnitTypes, gUnit:GetTypeName()) then
                                    anyOfTypeAlive = false
                                end
                            end
                        end)
                        return anyOfTypeAlive
                    end)
                end

                function task.instance:OnAfterSuccess(From, Event, To)
                    task.state = "finished"
                    checkObjectiveCapture(objective)
                    saveState()
                end

                MissionDb.strandtasks.instance:AddPlayerTaskToQueue(task.instance)
            elseif taskAuftrag == "BOMBING" then
                local taskGroupTargetNameContains = taskZone:GetProperty("groupTargetNameContains")
                local taskStaticTargetNameContains = taskZone:GetProperty("staticTargetNameContains")

                local possibleSets = {}

                if taskGroupTargetNameContains ~= "" then
                    local set = SET_GROUP:New():FilterCoalitions("red"):FilterPrefixes(taskGroupTargetNameContains):FilterStart()
                    table.insert(possibleSets, set)
                end

                if taskStaticTargetNameContains ~= "" then
                    local set = SET_STATIC:New():FilterCoalitions("red"):FilterPrefixes(taskStaticTargetNameContains):FilterStart()
                    table.insert(possibleSets, set)
                end

                local sceneryTargetZoneNames = taskZone:GetProperty("sceneryTargetZoneNames")
                if sceneryTargetZoneNames ~= "" then
                    local zones = split(sceneryTargetZoneNames, ",")
                    for _, zoneName in ipairs(zones) do
                        local set = SET_SCENERY:NewFromZone(zoneName)
                        table.insert(possibleSets, set)
                    end
                end

                local target = TARGET:New(possibleSets[1])

                for i, s in ipairs(possibleSets) do
                    if i > 1 then
                        target:AddObject(s)
                    end
                end

                task.instance = PLAYERTASK:New(AUFTRAG.Type.BOMBING, target, true , 99, "")
                task.instance:SetMenuName(taskLabel)
                task.instance:AddFreetext(taskDescription)

                -- todo, include the targetTypes stuff

                function task.instance:OnAfterSuccess(From, Event, To)
                    for _, s in ipairs(possibleSets) do
                        s:FilterStop()
                    end
                    task.state = "finished"
                    checkObjectiveCapture(objective)
                    saveState()
                end

                MissionDb.strandtasks.instance:AddPlayerTaskToQueue(task.instance)
            elseif taskAuftrag == "CSAR" then
                local targetZoneName = taskZone:GetProperty("targetZone")
                local targetName = taskZone:GetProperty("targetName")
                local targetZone = ZONE:FindByName(targetZoneName)

                local target = TARGET:New(targetZone)
                task.instance = PLAYERTASK:New(AUFTRAG.Type.CSAR, target, true , 99, "")
                task.instance:SetSubType("Boarded")
                task.instance:SetMenuName(taskLabel)
                task.instance:AddFreetext(taskDescription)
                task.instance.CSARPilotName = targetName
                task.instance.SmokeColor = SMOKECOLOR.Blue
                function task.instance:OnAfterSuccess(From, Event, To)
                    task.state = "finished"
                    checkObjectiveCapture(objective)
                    saveState()
                end
                MissionDb.strandtasks.instance:AddPlayerTaskToQueue(task.instance)
                MissionDb.csar.instance:AddPlayerTask(task.instance)

                MissionDb.csar.instance:SpawnCSARAtZone(targetZone, coalition.side.BLUE, targetName, true, true, nil, nil, true)
            end
        end
    end

    unlockFarpsForObjective(objective)
    unlockAirbasesForObjective(objective)
    unlockReinforcementsForObjective(objective)
    unlockQrfsForObjective(objective)

    objective.state = "active"

    saveState()

    SCHEDULER:New(nil, function()
        showObjectiveStartedUpdate(objective)
    end, {}, 5)

    local nextObjective = determineNextObjectiveFrom(objective)
    if nextObjective ~= nil then
        local nextObjectiveZone = ZONE:FindByName(nextObjective.name)
        if nextObjectiveZone:Get2DDistance(objectiveZone:GetCoordinate(0)) > 37040 then
            SCHEDULER:New(nil, function()
                spawnGroupsAtThing(nextObjective, country.id.CJTF_RED)
            end, {}, 270)
        end
    end
end

local function spawnCasevacForCompletedObjective(objective)
    local objectiveZone = ZONE:FindByName(objective.name)
    local objectiveLabel = objectiveZone:GetProperty("label")
    local count = math.random(1, #objective.nodes)
    for i=1, count do
        MissionDb.csar.instance:SpawnCASEVAC(objectiveZone:GetRandomPointVec2(), coalition.side.BLUE, string.format("%s casualty", objectiveLabel), true, 'absolute unit', 'whatever', true)
    end
    return count
end

local function progressToNextObjectiveFrom(completedObjective, strandName)
    local strand
    for _, s in ipairs(MissionDb.strands) do
        if s.name == strandName then
            strand = s
            break
        end
    end

    local toStartName = nil
    local strandComplete = false
    local missionComplete = false

    if completedObjective == nil then
        -- we don't know which one, so figure it out...
        local strandStateMap = {}
        for _, objectiveName in ipairs(strand.sequence) do
            for _, objective in ipairs(MissionDb.objectives) do
                if objective.name == objectiveName then
                    strandStateMap[objectiveName] = objective.state
                end
            end
        end

        for _, objectiveName in ipairs(strand.sequence) do
            local state = strandStateMap[objectiveName]
            if state == "active" or state == "unstarted" then
                toStartName = objectiveName
                break
            end
        end

        if toStartName == nil then
            strandComplete = true
            -- this strand is done, but we need to check the others before we reset it
            local anyObjectiveNotFinished = false
            for _, objective in ipairs(MissionDb.objectives) do
                if objective.strand ~= strandName and state ~= "finished" then
                    anyObjectiveNotFinished = true
                    break
                end
            end
            if not anyObjectiveNotFinished then
                missionComplete = true
            end
        end
    else
        for i, objectiveName in ipairs(strand.sequence) do
            if objectiveName == completedObjective.name then
                local nextIndex = i+1
                if nextIndex <= #strand.sequence then
                    toStartName = strand.sequence[i+1]
                    break
                else
                    strandComplete = true
                    local anyObjectiveNotFinished = false
                    for _, objective in ipairs(MissionDb.objectives) do
                        if objective.state ~= "finished" then
                            anyObjectiveNotFinished = true
                            break
                        end
                    end

                    if not anyObjectiveNotFinished then
                        missionComplete = true
                    end
                end
            end
        end

        local casevacCount = spawnCasevacForCompletedObjective(completedObjective)

        showObjectiveCompletedUpdate(completedObjective, strandName, casevacCount)
    end

    if toStartName == nil then
        if missionComplete then
            -- Do end of mission stuff
            MESSAGE:New("MISSION COMPLETE -- NOBODY WINS!!!", 5):ToAll()
        elseif strandComplete then
            -- Do end of strand stuff
            MESSAGE:New(strandName .. " COMPLETE", 5):ToAll()
        end
    else
        for _, objective in ipairs(MissionDb.objectives) do
            if objective.name == toStartName then
                if completedObjective == nil then
                    startObjective(objective)
                else
                    local delay = 120
                    MESSAGE:New(string.format("STRAND UPDATE\n\n%s will be progressing to the next objective in %s seconds", strandName, delay), 30):ToAll()
                    SCHEDULER:New(nil, function()
                        startObjective(objective)
                    end, {}, delay)
                end
                break
            end
        end
    end
end

completeObjective = function(objective, killLinkedUnits)
    if #objective.nodes > 0 then
        UTILS.RemoveMark(objective.labelMarkId, 0)

        MissionDb.redchief.conflictZones:RemoveZonesByName(objective.name)
        MissionDb.bluechief.conflictZones:RemoveZonesByName(objective.name)
    end

    for _, node in ipairs(objective.nodes) do
        node.opsZone:SetDrawZone(false)
        node.opsZone:GetZone():UndrawZone()
        node.opsZone:Stop()
        UTILS.RemoveMark(node.labelMarkId, 0)
        MissionDb.ctld.instance:DeactivateZone(node.name, CTLD.CargoZoneType.MOVE)
    end

    if killLinkedUnits then
        for _, category in ipairs({objective.vehicleGroups, objective.shipGroups}) do
            for _, group in ipairs(category) do
                local group = GROUP:FindByName(group.name)
                group:Destroy(true)
            end
        end
    end

    for _, task in ipairs(objective.tasks) do
        task.state = "finished"
        if task.instance then
            task.instance:__Success(-1)
            if killLinkedUnits then
                for _, category in ipairs({task.vehicleGroups, task.shipGroups}) do
                    for _, group in ipairs(category) do
                        local group = GROUP:FindByName(group.name)
                        group:Destroy(true)
                    end
                end
            end
        end
    end

    objective.state = "finished"

    saveState()

    if(objective.completeSound ~= "") then
        SCHEDULER:New(nil, function()
            local playItAgainSam = USERSOUND:New(objective.completeSound)
            playItAgainSam:ToAll()
        end, {}, 5)
    end

    progressToNextObjectiveFrom(objective, objective.strand)
end

local function lockAllFarpSlots()
    for _, objective in ipairs(MissionDb.objectives) do
        for _, farp in ipairs(objective.farps) do
            for _, client in ipairs(farp.clients) do
                local farpSlot = USERFLAG:New(client)
                farpSlot:Set(100)
            end
        end
    end
end

local function lockAllAirbaseSlots()
    for _, objective in ipairs(MissionDb.objectives) do
        for _, airbase in ipairs(objective.airbases) do
            for _, client in ipairs(airbase.clients) do
                local airbaseSlot = USERFLAG:New(client)
                airbaseSlot:Set(100)
            end
        end
    end
end

local function initializeRedChief()
    local redAgents = SET_GROUP:New():FilterCoalitions("red"):FilterStart()
    MissionDb.redchief.instance = CHIEF:New(coalition.side.RED, redAgents, "Red Chief")
    MissionDb.redchief.instance:SetTacticalOverviewOn()
    MissionDb.redchief.instance:SetStrategy(CHIEF.Strategy.AGGRESSIVE)
    MissionDb.redchief.conflictZones = SET_ZONE:New()
    MissionDb.redchief.instance:SetConflictZones(MissionDb.redchief.conflictZones)
end

local function initializeBlueChief()
    local blueAgents = SET_GROUP:New():FilterCoalitions("blue"):FilterStart()
    MissionDb.bluechief.instance = CHIEF:New(coalition.side.BLUE, blueAgents, "Blue Chief")
    -- MissionDb.bluechief.instance:SetTacticalOverviewOn()
    MissionDb.bluechief.instance:SetStrategy(CHIEF.Strategy.DEFENSIVE)
    MissionDb.bluechief.conflictZones = SET_ZONE:New()
    MissionDb.bluechief.instance:SetConflictZones(MissionDb.bluechief.conflictZones)

    local blueAwacsZone = ZONE:FindByName("BLUE AWACS ZONE")
    if blueAwacsZone then
        MissionDb.bluechief.instance:AddAwacsZone(blueAwacsZone)
    end

    local blueUAVzone = ZONE:FindByName("BLUE UAV ZONE")
    if blueUAVZone then
        MissionDb.bluechief.instance:AddUAVzone(blueUAVZone)
    end
end

local function initializeRedChief2()
    for _, airwing in ipairs(MissionDb.redchief.airwings) do
        if airwing.state == "active" then
            airwing.instance = AIRWING:New(airwing.warehouse, airwing.name)

            function airwing.instance:OnAfterAirbaseCaptured(From, Event, To, Coalition)
                MESSAGE:New("AIRBASE CAPTURED!", 15):ToAll()
                if Coalition == coalition.side.BLUE then
                    SCHEDULER:New(nil, function()
                        airwing.state = "dead"
                        STATIC:FindByName(airwing.warehouse):GetCoordinate():Explosion(999)
                        local text=string.format("Friendly forces have destroyed the enemy airwing at %s.", airwing.airbase)
                        MESSAGE:New(text, 15):ToAll()
                    end, {}, 1)
                end
            end

            function airwing.instance:OnAfterFlightOnMission(From, Event, To, Flightgroup, Mission)
                if Mission:GetType() == AUFTRAG.Type.BOMBCARPET or Mission:GetType() ~= AUFTRAG.Type.BAI then
                    if math.random(1, 100) <= 25 then
                        local escortMission = AUFTRAG:NewESCORT(Flightgroup:GetGroup())
                        MissionDb.redchief.instance:AddMission(escortMission)
                    end
                end

                local text=string.format("RED has launched a new mission: %s.", Mission:GetType())
                MESSAGE:New(text, 15):ToAll()
            end

            for _, squadron in ipairs(airwing.squadrons) do
                squadron.instance = SQUADRON:New(squadron.templateGroupName, squadron.initialInventory, squadron.name)
                squadron.instance:SetSkill(AI.Skill.EXCELLENT)
                squadron.instance:SetTakeoffHot()
                for _, capability in ipairs(squadron.capabilities) do
                    squadron.instance:AddMissionCapability({capability.mission}, capability.performance)
                end
                squadron.instance:SetLivery(squadron.livery)

                airwing.instance:AddSquadron(squadron.instance)
                for _, payload in ipairs(squadron.payloads) do
                    airwing.instance:NewPayload(GROUP:FindByName(payload.templateGroupName), -1, payload.missionTypes)
                end
            end
            MissionDb.redchief.instance:AddAirwing(airwing.instance)
        end
    end

    MissionDb.redchief.instance:__Start(15)
end

local function initializeBlueChief2()
    for _, airwing in ipairs(MissionDb.bluechief.airwings) do
        if airwing.state == "active" then
            airwing.instance = AIRWING:New(airwing.warehouse, airwing.name)

            function airwing.instance:OnAfterFlightOnMission(From, Event, To, Flightgroup, Mission)
                local text=string.format("BLUE has launched a new mission: %s.", Mission:GetType())
                MESSAGE:New(text, 15):ToAll()
            end

            for _, squadron in ipairs(airwing.squadrons) do
                squadron.instance = SQUADRON:New(squadron.templateGroupName, squadron.initialInventory, squadron.name)
                squadron.instance:SetSkill(AI.Skill.EXCELLENT)
                squadron.instance:SetTakeoffHot()
                for _, capability in ipairs(squadron.capabilities) do
                    squadron.instance:AddMissionCapability({capability.mission}, capability.performance)
                end
                squadron.instance:SetLivery(squadron.livery)

                airwing.instance:AddSquadron(squadron.instance)
                for _, payload in ipairs(squadron.payloads) do
                    airwing.instance:NewPayload(GROUP:FindByName(payload.templateGroupName), -1, payload.missionTypes)
                end
            end
            MissionDb.bluechief.instance:AddAirwing(airwing.instance)
        end
    end

    MissionDb.bluechief.instance:__Start(15)
end

local function initializeObjectives()
    loadState()
    saveState()

    lockAllFarpSlots()
    lockAllAirbaseSlots()
    initializeRedChief()
    initializeBlueChief()

    local strandInProgressCount = {}

    for _, strand in ipairs(MissionDb.strands) do
        strandInProgressCount[strand.name] = 0
    end

    local finishedCount = 0

    for _, objective in ipairs(MissionDb.objectives) do
        if objective.state == "active" then
            startObjective(objective)
            strandInProgressCount[objective.strand] = strandInProgressCount[objective.strand] + 1
        elseif objective.state == "finished" then
            finishedCount = finishedCount + 1
            unlockFarpsForObjective(objective)
            unlockAirbasesForObjective(objective)
            unlockReinforcementsForObjective(objective)
            unlockQrfsForObjective(objective)
        end
    end

    SCHEDULER:New(nil, function()
        initializeBlueChief2()
        initializeRedChief2()
    end, {}, 60)

    -- All finished so reset them so it can start over
    if(finishedCount == #MissionDb.objectives) then
        -- ALL DONE, go reset things...
    end

    for strandName, count in pairs(strandInProgressCount) do
        if count == 0 then
            progressToNextObjectiveFrom(nil, strandName)
        end
    end
end

local function debugCompleteObjective(menuArgs)
    for _, objective in ipairs(MissionDb.objectives) do
        if objective.state == "active" and objective.strand == menuArgs.strand then
            completeObjective(objective, menuArgs.killLinkedUnits)
            break
        end
    end
end

local function reportOverallMissionStatus()
    local strandObjectiveStateMap = buildStrandObjectiveStateMap()

    local r = {}
    table.insert(r, "MISSION STATUS")
    table.insert(r, "")
    for strandName, props in pairs(strandObjectiveStateMap) do
        table.insert(r,string.format("%s, %i/%i objectives complete", strandName, props.finished, props.total))
        if(props.active and props.finished ~= props.total) then
            table.insert(r,string.format("  %s", props.activeObjective.displayName))
            if props.activeObjective.totalNodes > 0 then
                table.insert(r,string.format("      %i/%i zones captured", props.activeObjective.capturedNodes, props.activeObjective.totalNodes))
                for _, node in ipairs(props.activeObjective.nodes) do
                    if node.captured then
                        table.insert(r,string.format("        - %s: captured", node.name))
                    else
                        table.insert(r,string.format("        - %s: %i enemy units", node.name, node.redUnitsCount))
                    end
                end
            end
            if props.activeObjective.totalTasks > 0 then
                table.insert(r,string.format("      %i/%i tasks completed", props.activeObjective.completedTasks, props.activeObjective.totalTasks))
                for _, task in ipairs(props.activeObjective.tasks) do
                    if task.complete then
                        table.insert(r,string.format("        - %s '%s': complete", task.auftrag, task.name))
                    else
                        table.insert(r,string.format("        - %s '%s': active", task.auftrag, task.name))
                    end
                end
            end
        end
        table.insert(r, "")
    end
    local m = table.concat(r, "\n")
    MESSAGE:New(m, 30):ToAll()
end

local function debugResupplySquadron(menuArgs)
    for _, airwing in ipairs(MissionDb.redchief.airwings) do
        if airwing.state == "active" then
            for _, squadron in ipairs(airwing.squadrons) do
                if squadron.name == menuArgs.name then
                    airwing.instance:AddAssetToSquadron(squadron.instance, 1)
                end
            end
        end
    end
end

local function debugResupplyAirwing(menuArgs)
    for _, airwing in ipairs(MissionDb.redchief.airwings) do
        if airwing.name == menuArgs.name and airwing.state == "active" then
            for _, squadron in ipairs(airwing.squadrons) do
                airwing.instance:AddAssetToSquadron(squadron.instance, 1)
            end
        end

    end
end


local function randomChiefMissions()
    local bombingPotentials = {}
    local baiPotentials = {}

    for _, objective in ipairs(MissionDb.objectives) do
        if objective.state == "active" then
            for _, node in ipairs(objective.nodes) do
                if node.state ~= "unstarted" then
                    node.opsZone:EvaluateZone()
                    if node.opsZone:IsGuarded() and node.opsZone:IsBlue() then
                        table.insert(bombingPotentials, {coordinate = node.opsZone:GetCoordinate(), zone = node.opsZone:GetZone() })
                    end
                end
            end

            local objectiveZone = ZONE:FindByName(objective.name)
            local groupsInZone = SET_GROUP:New():FilterActive():FilterCoalitions("blue"):FilterZones({objectiveZone}):FilterOnce()
            groupsInZone:ForEachGroup(function(g)
                table.insert(baiPotentials, g)
            end)
        end
    end

    if #bombingPotentials > 0 then
        local chosen = bombingPotentials[math.random(#bombingPotentials)]

        local bombingMission = AUFTRAG:NewBOMBCARPET(chosen.coordinate, 10000, 500)
        MissionDb.redchief.instance:AddMission(bombingMission)
    end

    if #baiPotentials > 0 then
        local chosenGroundTargetGroup = baiPotentials[math.random(#baiPotentials)]
        local baiMission = AUFTRAG:NewBAI(chosenGroundTargetGroup)
        MissionDb.redchief.instance:AddMission(baiMission)
    end
end

local function initializeStrandMenus()
    local menuMissionStatus = MENU_MISSION:New("Mission Status")
    MENU_MISSION_COMMAND:New("Overall Status", menuMissionStatus, reportOverallMissionStatus)

    if MissionDb.devmode then
        local menuDebug = MENU_MISSION:New("Debug", menuMissionStatus)
        local menuDebugStrands = MENU_MISSION:New("Strands", menuDebug)
        for _, strand in ipairs(MissionDb.strands) do
            local menuIndividualStrand = MENU_MISSION:New(strand.name, menuDebugStrands)
            MENU_MISSION_COMMAND:New("Complete (kill units)", menuIndividualStrand, debugCompleteObjective, {strand = strand.name, killLinkedUnits = true})
            MENU_MISSION_COMMAND:New("Complete (leave units)", menuIndividualStrand, debugCompleteObjective, {strand = strand.name, killLinkedUnits = false})
        end

        MENU_MISSION_COMMAND:New("Save", menuDebug, saveState)
        MENU_MISSION_COMMAND:New("Spawn QRF", menuDebug, randomEnemyReinforcement)
        MENU_MISSION_COMMAND:New("Spawn Enemy Air Missions", menuDebug, randomChiefMissions)
        MENU_MISSION_COMMAND:New("Spawn Friendly Reinforcement", menuDebug, randomFriendlyReinforcement)


        local menuDebugSquadronResupply = MENU_MISSION:New("Resupply Squadrons", menuDebug)
        for _, airwing in ipairs(MissionDb.redchief.airwings) do
            if airwing.state == "active" then
                MENU_MISSION_COMMAND:New(squadron.templateGroupName, menuDebugSquadronResupply, debugResupplySquadron, { name = squadron.name, state = airwing.state })
            end
        end

        local menuDebugAirwingResupply = MENU_MISSION:New("Resupply Airwings", menuDebug)
        for _, airwing in ipairs(MissionDb.redchief.airwings) do
            MENU_MISSION_COMMAND:New(airwing.name, menuDebugAirwingResupply, debugResupplyAirwing, { name = airwing.name, state = airwing.state })
        end
    end
end

local function initializeCtld()
    MissionDb.ctld.instance = CTLD:New(coalition.side.BLUE, MissionDb.ctld.groups, "CTLD Rotary Gang")

    MissionDb.ctld.instance.dropcratesanywhere = true
    MissionDb.ctld.instance.forcehoverload = false
    MissionDb.ctld.instance.hoverautoloading = false
    MissionDb.ctld.instance.movetroopsdistance  = 1000
    MissionDb.ctld.instance.enableHercules = false
    MissionDb.ctld.instance.enableslingload = true
    MissionDb.ctld.instance.cratecountry = country.id.CJTF_BLUE
    MissionDb.ctld.instance.buildtime = 0

    MissionDb.ctld.instance.enableLoadSave = true
    MissionDb.ctld.instance.saveinterval = 600
    MissionDb.ctld.instance.filename = "ctld.csv"
    MissionDb.ctld.instance.filepath = defaultDrive
    MissionDb.ctld.instance.eventoninject = true

    MissionDb.ctld.instance:Start()
    MissionDb.ctld.instance:AddTroopsCargo("Infantry (8)", { "CTLD Inf M4 8" }, CTLD_CARGO.Enum.TROOPS, 8, 80)
    MissionDb.ctld.instance:AddTroopsCargo("Infantry - AA (6)", { "CTLD Infantry AA" }, CTLD_CARGO.Enum.TROOPS, 6, 80)
    MissionDb.ctld.instance:AddTroopsCargo("Infantry - AT (8)", { "CTLD Infantry AT" }, CTLD_CARGO.Enum.TROOPS, 8, 80)
    MissionDb.ctld.instance:AddTroopsCargo("JTAC (1)", { "CTLD BLUE RECCE JTAC" }, CTLD_CARGO.Enum.TROOPS, 1, 80)
    MissionDb.ctld.instance:AddTroopsCargo("MORTAR (5)", { "CTLD MORTAR" }, CTLD_CARGO.Enum.TROOPS, 5, 122)

    MissionDb.ctld.instance:AddCratesCargo("HMMWV - JTAC", { "CTLD BLUE RECCE JTAC HMMWV" }, CTLD_CARGO.Enum.VEHICLE, 1, 1350)
    MissionDb.ctld.instance:AddCratesCargo("HMMWV - MG", { "CTLD HMMWV MG" }, CTLD_CARGO.Enum.VEHICLE, 1, 1350)
    MissionDb.ctld.instance:AddCratesCargo("HMMWV - TOW", { "CTLD HMMWV TOW" }, CTLD_CARGO.Enum.VEHICLE, 1, 1350)
    MissionDb.ctld.instance:AddCratesCargo("AVENGER", { "CTLD AVENGER" }, CTLD_CARGO.Enum.VEHICLE, 1, 1350)
    MissionDb.ctld.instance:AddCratesCargo("M939 - AMMO", { "CTLD M818" }, CTLD_CARGO.Enum.VEHICLE, 1, 1350)
    MissionDb.ctld.instance:AddCratesCargo("M60A3", { "CTLD M60" }, CTLD_CARGO.Enum.VEHICLE, 2, 1350)
    MissionDb.ctld.instance:AddCratesCargo("STRYKER - MGS", { "CTLD STRYKER MGS" }, CTLD_CARGO.Enum.VEHICLE, 1, 1350)
    MissionDb.ctld.instance:AddCratesCargo("STRYKER - ICV", { "CTLD STRYKER ICV" }, CTLD_CARGO.Enum.VEHICLE, 1, 1350)
    MissionDb.ctld.instance:AddCratesCargo("HAWK Launcher", { "CTLD HAWK LN" }, CTLD_CARGO.Enum.VEHICLE, 1, 1350)
    MissionDb.ctld.instance:AddCratesCargo("HAWK Search Radar", { "CTLD HAWK SR" }, CTLD_CARGO.Enum.VEHICLE, 1, 1350)
    MissionDb.ctld.instance:AddCratesCargo("HAWK Track Radar", { "CTLD HAWK TR" }, CTLD_CARGO.Enum.VEHICLE, 1, 1350)
    MissionDb.ctld.instance:AddCratesCargo("HAWK PCP", { "CTLD HAWK PCP" }, CTLD_CARGO.Enum.VEHICLE, 1, 1350)
    MissionDb.ctld.instance:AddCratesCargo("HAWK CWAR", { "CTLD HAWK CWAR" }, CTLD_CARGO.Enum.VEHICLE, 1, 1350)

    CTLD_HERCULES:New(coalition.side.BLUE, "Jaelifter Fixed Wing", MissionDb.ctld.instance)

    function MissionDb.ctld.instance:OnAfterTroopsPickedUp(From, Event, To, Group, Unit, Cargo)
        MESSAGE:New(string.format("%s loaded '%s' into a %s.", Unit:GetPlayerName(), Cargo.Name, Unit:GetTypeName()), 5):ToAll()
    end

    function MissionDb.ctld.instance:OnAfterTroopsDeployed(From, Event, To, Group, Unit, Troops)
        if Unit then
            MESSAGE:New(string.format("%s deployed troops into the field from a %s.", Unit:GetPlayerName(), Unit:GetTypeName()), 5):ToAll()
        end

        local g = Troops
        g:HandleEvent( EVENTS.Dead )
        function g:OnEventDead( EventData )
            -- 100% of the time...
            if math.random(1, 100) <= MissionDb.settings.blueCasevacChance then
                local c = EventData.IniGroup:GetCoordinate()
                if c then
                    MissionDb.csar.instance:SpawnCASEVAC(c:Translate(math.random(1, 10), math.random(0, 359)), coalition.side.BLUE, "CASEVAC", false, "CASEVAC", "CASEVAC", true)
                end
            end
        end
    end

    function MissionDb.ctld.instance:OnAfterTroopsExtracted(From, Event, To, Group, Unit, Troops)
        MESSAGE:New(string.format("%s extracted troops from the field in a %s.", Unit:GetPlayerName(), Unit:GetTypeName()), 5):ToAll()
    end

    function MissionDb.ctld.instance:OnAfterCratesPickedUp(From, Event, To, Group, Unit, Cargo)
        MESSAGE:New(string.format("%s loaded a crate for '%s' into a %s.", Unit:GetPlayerName(), Cargo.Name, Unit:GetTypeName()), 5):ToAll()
    end

    function MissionDb.ctld.instance:OnAfterCratesDropped(From, Event, To, Group, Unit, Cargotable)
        MESSAGE:New(string.format("%s dropped crates into the field from a %s.", Unit:GetPlayerName(), Unit:GetTypeName()), 5):ToAll()
    end

    function MissionDb.ctld.instance:OnAfterCratesBuild(From, Event, To, Group, Unit, Vehicle)
        if Unit then
            MESSAGE:New(string.format("%s built crates into a %s.", Unit:GetPlayerName(), Vehicle:GetTypeName()), 5):ToAll()
        end

        local g = Vehicle
        g:HandleEvent( EVENTS.Dead )
        function g:OnEventDead( EventData )
            -- 100% of the time...
            if math.random(1, 100) <= MissionDb.settings.blueCasevacChance then
                local c = EventData.IniGroup:GetCoordinate()
                if c then
                    MissionDb.csar.instance:SpawnCASEVAC(c:Translate(math.random(1, 10), math.random(0, 359)), coalition.side.BLUE, "CASEVAC", false, "CASEVAC", "CASEVAC", true)
                end
            end
        end
    end

    MissionDb.ctld.instance:__Load(5)
end

local function initializeCsar()
    MissionDb.csar.instance = CSAR:New(coalition.side.BLUE, "Downed Pilot")

    MissionDb.csar.instance.csarPrefix = MissionDb.csar.groups
    MissionDb.csar.instance.allowDownedPilotCAcontrol  = true
    MissionDb.csar.instance.countryblue = country.id.UN_PEACEKEEPERS
    MissionDb.csar.instance.enableForAI = true
    MissionDb.csar.instance.csarUsePara = true
    MissionDb.csar.instance.allowbronco = true
    MissionDb.csar.instance.autosmoke = true

    function MissionDb.csar.instance:OnAfterRescued(from, event, to, heliunit, heliname, pilotssaved)
        local potentials = {}
        for _, objective in ipairs(MissionDb.objectives) do
            if objective.state == "active" then
                for _, group in ipairs(objective.vehicleGroups) do
                    if group.state == "active" then
                        table.insert(potentials, group.name)
                    end
                end
            end
        end

        MESSAGE:New(string.format("%i lives were saved! They'll be debriefed and any intel will be made available shortly.", pilotssaved), 5):ToAll()

        if #potentials > 0 then
            local count = math.random(1, pilotssaved)
            for i=1, count do
                local chosen = potentials[math.random(#potentials)]
                MissionDb.csar.taskControllerInstance:AddTarget(GROUP:FindByName(chosen):GetCoordinate())
            end

            randomFriendlyReinforcement()
        end
    end

    MissionDb.csar.instance:Start()
end

local function initializeAutolase()
    SCHEDULER:New(nil, function()
        local jtacs = SET_GROUP:New():FilterPrefixes("JTAC"):FilterCoalitions("blue"):FilterStart()
        MissionDb.autolase.instance = AUTOLASE:New(jtacs,coalition.side.BLUE)
        MissionDb.autolase.instance:SetSmokeTargets(true, SMOKECOLOR.Orange)
        MissionDb.autolase.instance:SetMaxLasingTargets(1)
        MissionDb.autolase.instance:SetLasingParameters(10000, 14400)
    end, {}, 60)
end

-- local function initializePlayerRecce()
--     local playerSet = SET_CLIENT:New():FilterCoalitions("blue"):FilterActive(true):FilterPrefixes({"SA342L", "SA342M", "Ka-50", "Bronco-OV-10A"}):FilterStart()
--     local attackers = SET_CLIENT:New():FilterCoalitions("blue"):FilterActive(true):FilterStart()
--     MissionDb.playerRecce.instance = PLAYERRECCE:New("PLAYER RECCE", coalition.side.BLUE, playerSet)
--     MissionDb.playerRecce.instance:SetAttackSet(attackers)
-- end

local function intializeStrandTaskController()
    MissionDb.strandtasks.instance = PLAYERTASKCONTROLLER:New("82nd Airborne", coalition.side.BLUE, PLAYERTASKCONTROLLER.Type.A2GS)
    MissionDb.strandtasks.instance:SetLocale("en")
    MissionDb.strandtasks.instance:SetMenuName("STRAND TASKS")
    MissionDb.strandtasks.instance:EnableTaskInfoMenu()
end

local function initializeCsarIntelTaskController()
    MissionDb.csar.taskControllerInstance = PLAYERTASKCONTROLLER:New("82nd Airborne", coalition.side.BLUE, PLAYERTASKCONTROLLER.Type.A2G)
    MissionDb.csar.taskControllerInstance:SetLocale("en")
    MissionDb.csar.taskControllerInstance:SetMenuName("CSAR INTEL TASKS")
    MissionDb.csar.taskControllerInstance:EnableTaskInfoMenu()
end

local function initializeMantis()
    MissionDb.samnetwork.instance = MANTIS:New("BlapBlap", "RED SAM", "RED EWR", nil, "red", true)
    MissionDb.samnetwork.instance:Start()
end

initializeCtld()

initializeCsar()

initializeStrandMenus()

intializeStrandTaskController()

initializeCsarIntelTaskController()

initializeAutolase()

initializeMantis()

-- initializePlayerRecce()

SCHEDULER:New(nil, initializeObjectives, {}, 30)

-- not ready for prime time


-- local function doIt()
--     STATIC:FindByName("RED TASK-3 TASK3TALKER COMMS TOWER-1#00001"):Destroy(true)
-- end

-- MENU_MISSION_COMMAND:New("Complete Tasks", nil, doIt)

MESSAGE:New("CALVINBALL END!", 5):ToAll()

SCHEDULER:New(nil, saveState, {}, 600, 600)

-- Dispatch a random enemy reinforcement to an active node somewhere between 30 and 60 minutes
-- after the game starts, and then every hour after that point.
SCHEDULER:New(nil, randomEnemyReinforcement, {}, math.random(1800, 3600), 3600)

-- Dispatch a random friendly reinforcement to an active node somewhere between 30 and 60 minutes
-- after the game starts, and then every hour after that point.
SCHEDULER:New(nil, randomFriendlyReinforcement, {}, math.random(1800, 3600), 3600)

-- Dispatch random chief missions somewhere between 5 and 10 minutes after the game starts
-- and every 30 minutes after that point.
SCHEDULER:New(nil, randomChiefMissions, {}, math.random(300, 600), 2700)

SCHEDULER:New(nil, standardAirwingReinforcement, {}, 120, 3600)