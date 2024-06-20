import moapy.project.wgsd.wgsd_flow as wgsd_flow
import moapy.project.wgsd.wgsd_sectionproperty as wgsd_sectionproperty
import moapy.mdreporter as mdreporter

from moapy.auto_convert import auto_schema

@auto_schema
def generate_report_3dpm(matl: wgsd_flow.gsdMaterial, geom: wgsd_flow.gsdGeometry, lcb: wgsd_flow.gsdLcb, opt: wgsd_flow.gsdOptions, sectprop: wgsd_sectionproperty.MSectionProperty):
    """
    Generate 3D PM report
    """
    rpt = mdreporter.ReportUtil("3dpm.md", "*3D PM Report*")
    rpt.add_chapter("Material")
    rpt.add_line(f"Concrete : {matl.concrete.grade.grade}")
    # rpt.add_line_fvu("f_{ck}", matl.concrete.grade.fck, mdreporter.enUnit.STRESS)
    # rpt.add_line_fvu("E_{c}", matl.concrete.grade.Ec, mdreporter.enUnit.STRESS)
    # SS-curve에 대한 정보를 추가

    rpt.add_line(f"Rebar : {matl.rebar.grade.grade}")
    # rpt.add_line_fvu("f_{yk}", matl.rebar.grade.fyk, mdreporter.enUnit.STRESS)
    # rpt.add_line_fvu("E_{s}", matl.rebar.grade.Es, mdreporter.enUnit.STRESS)
    # SS-curve에 대한 정보를 추가

    rpt.add_chapter("Section")
    # 삽도?
    rpt.add_line_fvu("Area", sectprop.DATA[0], mdreporter.enUnit.AREA)
    rpt.add_line_fvu("Asy", sectprop.DATA[1], mdreporter.enUnit.AREA)
    rpt.add_line_fvu("Asz", sectprop.DATA[2], mdreporter.enUnit.AREA)
    rpt.add_line_fvu("Ixx", sectprop.DATA[3], mdreporter.enUnit.INERTIA)
    rpt.add_line_fvu("Iyy", sectprop.DATA[4], mdreporter.enUnit.INERTIA)
    rpt.add_line_fvu("Izz", sectprop.DATA[5], mdreporter.enUnit.INERTIA)
    rpt.add_line_fvu("Cy", sectprop.DATA[6], mdreporter.enUnit.LENGTH)
    rpt.add_line_fvu("Cz", sectprop.DATA[7], mdreporter.enUnit.LENGTH)
    rpt.add_line_fvu("Syp", sectprop.DATA[8], mdreporter.enUnit.LENGTH)
    rpt.add_line_fvu("Sym", sectprop.DATA[9], mdreporter.enUnit.LENGTH)
    rpt.add_line_fvu("Szp", sectprop.DATA[10], mdreporter.enUnit.LENGTH)
    rpt.add_line_fvu("Szm", sectprop.DATA[11], mdreporter.enUnit.LENGTH)
    rpt.add_line_fvu("Ipyy", sectprop.DATA[12], mdreporter.enUnit.INERTIA)
    rpt.add_line_fvu("Ipzz", sectprop.DATA[13], mdreporter.enUnit.INERTIA)
    rpt.add_line_fvu("Zy", sectprop.DATA[14], mdreporter.enUnit.AREA)
    rpt.add_line_fvu("Zz", sectprop.DATA[15], mdreporter.enUnit.AREA)
    rpt.add_line_fvu("ry", sectprop.DATA[16], mdreporter.enUnit.LENGTH)
    rpt.add_line_fvu("rz", sectprop.DATA[17], mdreporter.enUnit.LENGTH)

    rpt.add_chapter("Load Combination")
    rpt.add_line("| Name  | Fx   | My   | Mz   |")
    rpt.add_line("|-------|------|------|------|")
    for lcb in lcb.uls.DATA:
        rpt.add_line(f"| {lcb[0]} | {lcb[1]} | {lcb[2]} | {lcb[3]} |")

    return rpt.get_md_text()


# matl = wgsd_flow.gsdMaterial()
# geom = wgsd_flow.gsdGeometry()
# lcb = wgsd_flow.gsdLcb()
# opt = wgsd_flow.gsdOptions()
# sectprop = wgsd_sectionproperty.MSectionProperty()

# md = generate_report_3dpm(matl, geom, lcb, opt, sectprop)
# print(md)