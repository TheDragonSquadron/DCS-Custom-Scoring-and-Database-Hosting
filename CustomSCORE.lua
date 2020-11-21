--- Moose Scoring ---
--- DCS SERVER SCORES ---
Scoring = SCORING:New( "DCS-SERVER-Scores" )

-- Turn off messages
SCORING:SetMessagesHit(Off)
SCORING:SetMessagesDestroy(Off)
SCORING:SetMessagesAddon(Off) 
SCORING:SetMessagesZone(Off)

--Points awarded on 1-10 scale for enemy kill
Scoring:SetScaleDestroyScore( 10 )
--Points deducted on 1-40 scale for friendly kill
Scoring:SetScaleDestroyPenalty( 40 )
