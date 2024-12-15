import re

ATECO_MAPPING = {
    '01': {
        'settore': 'Agricoltura, Silvicoltura e Pesca',
        'sottocategorie': {
            '0111': 'Allevamento',
            '0112': 'Apicoltura',
            '0113': 'Coltivazione',
            '0114': 'Pesca',
            '0115': 'Silvicoltura',
            '0116': 'Agroindustria/Agroalimentare',
        }
    },
    '02': {
        'settore': 'Artigianato',
        'sottocategorie': {
            '0211': 'Artigianato Tipico',
            '0212': 'Produzione Artigianale di Beni',
        }
    },
    '45': {
        'settore': 'Commercio',
        'sottocategorie': {
            '4511': 'Commercio al dettaglio',
            '4512': 'Commercio all’ingrosso',
        }
    },
    '85': {
        'settore': 'Pubblico',
        'sottocategorie': {
            '8511': 'Amministrazione pubblica',
            '8512': 'Ente di ricerca pubblico',
            '8513': 'Istruzione scolastica pubblica',
            '8514': 'Istruzione universitaria pubblica',
            '8515': 'Sanità e assistenza sociale pubblica',
        }
    },
    '62': {
        'settore': 'Servizi',
        'sottocategorie': {
            '6211': 'Produzione di software',
            '6212': 'Consulenza informatica',
            '6213': 'Attività connesse',
            '6221': 'Audiovisivo/Media/Cinema',
            '6222': 'Ristorazione',
            '6223': 'Consulenza',
            '6224': 'Editoria/Informazione/Comunicazione',
            '6225': 'Formazione',
            '6226': 'Istruzione privata',
            '6227': 'Sanità privata',
            '6228': 'Servizi bancari/Assicurativi/Finanziari',
            '6229': 'Sport/Intrattenimento',
            '6230': 'Trasporti',
            '6240': 'Turismo',
            '6241': 'Strutture ricettive (Alberghi, Villaggi turistici, Campeggi, Rifugi di montagna, ecc.)',
            '6242': 'Agenzie di viaggio',
        }
    },
}

def get_sector_and_subcategory(code):
    """
    Determina il settore e la sottocategoria basandosi sul codice ATECO fornito.
    """
    code = code.strip()
    if not re.fullmatch(r'\d{4,6}', code):
        return None, None, "Il codice ATECO deve essere composto da 4 a 6 cifre numeriche."
    sector_code = code[:2]
    sector_info = ATECO_MAPPING.get(sector_code)
    
    if not sector_info:
        return None, None, f"Settore non trovato per il codice ATECO '{sector_code}'."
    
    settore = sector_info['settore']
    subcategory_code = code[:4]
    sottocategoria = sector_info['sottocategorie'].get(subcategory_code)
    
    if not sottocategoria:
        return settore, None, f"Sottocategoria non trovata per il codice ATECO '{subcategory_code}'."
    
    return settore, sottocategoria, None
