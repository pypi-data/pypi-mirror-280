from typing import List

from ninja import NinjaAPI

from django.db.models import Q

from ledger import app_settings
from ledger.api import schema
from ledger.api.helpers import (
    get_alts_queryset,
    get_main_character,
    get_models_and_string,
)
from ledger.hooks import get_extension_logger

_, CharacterWalletJournalEntry = get_models_and_string()

logger = get_extension_logger(__name__)


class LedgerJournalApiEndpoints:
    tags = ["CharacerJournal"]

    def __init__(self, api: NinjaAPI):

        @api.get(
            "account/{character_id}/wallet/",
            response={200: List[schema.CharacterWalletEvent], 403: str},
            tags=self.tags,
        )
        def get_character_wallet(
            request, character_id: int, type_refs: str = "", page: int = 1
        ):
            if character_id == 0:
                character_id = request.user.profile.main_character.character_id
            response, main = get_main_character(request, character_id)

            if not response:
                return 403, "Permission Denied"

            characters = get_alts_queryset(main)

            filters = (
                Q(character__eve_character__in=characters)
                if app_settings.LEDGER_MEMBERAUDIT_USE
                else Q(character__character__in=characters)
            )

            wallet_journal = CharacterWalletJournalEntry.objects.filter(
                filters
            ).select_related("first_party", "second_party")
            output = []

            start_count = (page - 1) * 10000
            end_count = page * 10000

            # pylint: disable=duplicate-code
            if type_refs:
                refs = type_refs.split(",")
                wallet_journal = wallet_journal.filter(ref_type__in=refs)

            wallet_journal = wallet_journal[start_count:end_count]

            for w in wallet_journal:
                output.append(
                    {
                        "character": (
                            w.character.character
                            if not app_settings.LEDGER_MEMBERAUDIT_USE
                            else w.character.eve_character
                        ),
                        "id": w.entry_id,
                        "date": w.date,
                        "first_party": {
                            "id": (
                                w.first_party.eve_id
                                if not app_settings.LEDGER_MEMBERAUDIT_USE
                                else w.first_party.id
                            ),
                            "name": w.first_party.name,
                            "cat": w.first_party.category,
                        },
                        "second_party": {
                            "id": (
                                w.second_party.eve_id
                                if not app_settings.LEDGER_MEMBERAUDIT_USE
                                else w.second_party.id
                            ),
                            "name": w.second_party.name,
                            "cat": w.second_party.category,
                        },
                        "ref_type": w.ref_type,
                        "amount": w.amount,
                        "balance": w.balance,
                        "reason": w.reason,
                    }
                )
            return output
