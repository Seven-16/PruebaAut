//Aaron Carmona 20231360
using System;
using System.Collections.Generic;

public class TardanzaServicio
{
    private List<Tardanza> _tardanza = new List<Tardanza>();
    public List<Tardanza> ObtenerTardanzas() => _tardanza;
    public void RegistrarTardanza(Tardanza tardanza)
    {
        tardanza.Id = _tardanza.Count + 1;
        tardanza.FechaHora = DateTime.Now;
        _tardanza.Add(tardanza);
    }
}

//Aaron Carmona 20231360